"""URL Shortener API - Day 30 capstone.

Concepts used: FastAPI, Pydantic validation, SQLite with parameterized
queries, indexes and uniqueness constraints, caching, rate limiting,
API-key authorization, logging, and testing.

Run:  uvicorn app:app --reload
Docs: http://127.0.0.1:8000/docs
"""

from __future__ import annotations

import logging
import os
import secrets
import sqlite3
import string
import time
from collections import defaultdict, deque
from contextlib import asynccontextmanager, closing
from functools import lru_cache

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import AnyHttpUrl, BaseModel

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("shortener")

DB_PATH = os.environ.get("DB_PATH", "shortener.db")
API_KEY = os.environ.get("API_KEY", "dev-secret-key")  # set a real one in production
ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 7
RATE_LIMIT = 10          # URL creations ...
RATE_WINDOW = 60         # ... per this many seconds, per client IP



@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title="URL Shortener", version="1.0.0", lifespan=lifespan)


# ---------- database ----------
def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with closing(get_conn()) as conn, conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS urls (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code   TEXT NOT NULL UNIQUE,
            original_url TEXT NOT NULL,
            created_at   TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS clicks (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            url_id     INTEGER NOT NULL REFERENCES urls(id) ON DELETE CASCADE,
            clicked_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            referrer   TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_clicks_url_id ON clicks(url_id);
        """)


def db():
    conn = get_conn()
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
    finally:
        conn.close()


# ---------- schemas ----------
class UrlCreate(BaseModel):
    url: AnyHttpUrl


class UrlOut(BaseModel):
    short_code: str
    short_url: str
    original_url: str


class StatsOut(BaseModel):
    short_code: str
    original_url: str
    created_at: str
    clicks: int


# ---------- helpers ----------
def generate_code() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


@lru_cache(maxsize=1024)
def _cached_lookup(code: str, db_path: str) -> tuple[int, str] | None:
    with closing(sqlite3.connect(db_path)) as conn:
        row = conn.execute(
            "SELECT id, original_url FROM urls WHERE short_code = ?", (code,)
        ).fetchone()
    return (row[0], row[1]) if row else None


_hits: dict[str, deque] = defaultdict(deque)


def rate_limit(request: Request) -> None:
    """Sliding-window limiter (in-memory; use Redis for multiple workers)."""
    ip = request.client.host if request.client else "unknown"
    now = time.monotonic()
    window = _hits[ip]
    while window and now - window[0] > RATE_WINDOW:
        window.popleft()
    if len(window) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests",
                            headers={"Retry-After": str(RATE_WINDOW)})
    window.append(now)


def require_api_key(x_api_key: str = Header(default="")) -> None:
    if not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


# ---------- routes ----------
@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/v1/urls", response_model=UrlOut, status_code=201,
          dependencies=[Depends(rate_limit)])
def create_url(payload: UrlCreate, request: Request, conn=Depends(db)) -> UrlOut:
    original = str(payload.url)
    for _ in range(5):                       # retry on (rare) code collision
        code = generate_code()
        try:
            with conn:
                conn.execute(
                    "INSERT INTO urls (short_code, original_url) VALUES (?, ?)",
                    (code, original))
            break
        except sqlite3.IntegrityError:
            logger.warning("Short code collision for %s, retrying", code)
    else:
        raise HTTPException(status_code=500, detail="Could not generate a unique code")

    logger.info("Created %s -> %s", code, original)
    return UrlOut(short_code=code,
                  short_url=f"{request.base_url}{code}",
                  original_url=original)


@app.get("/api/v1/urls/{code}/stats", response_model=StatsOut)
def stats(code: str, conn=Depends(db)) -> StatsOut:
    row = conn.execute("""
        SELECT u.short_code, u.original_url, u.created_at, COUNT(c.id) AS clicks
        FROM urls u LEFT JOIN clicks c ON c.url_id = u.id
        WHERE u.short_code = ?
        GROUP BY u.id
    """, (code,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Short code not found")
    return StatsOut(**dict(row))


@app.delete("/api/v1/urls/{code}", status_code=204,
            dependencies=[Depends(require_api_key)])
def delete_url(code: str, conn=Depends(db)) -> None:
    with conn:
        cur = conn.execute("DELETE FROM urls WHERE short_code = ?", (code,))
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Short code not found")
    _cached_lookup.cache_clear()


@app.get("/{code}")
def redirect(code: str, request: Request, conn=Depends(db)) -> RedirectResponse:
    found = _cached_lookup(code, DB_PATH)
    if found is None:
        raise HTTPException(status_code=404, detail="Short code not found")
    url_id, original = found
    with conn:
        conn.execute("INSERT INTO clicks (url_id, referrer) VALUES (?, ?)",
                     (url_id, request.headers.get("referer")))
    return RedirectResponse(original, status_code=307)
