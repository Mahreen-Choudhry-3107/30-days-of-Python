# Project 06: URL Shortener API (Capstone)

**Day 30 capstone** | Difficulty: ⭐⭐⭐⭐

A REST API that shortens URLs, redirects visitors, tracks clicks, and exposes statistics.

## Setup

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open <http://127.0.0.1:8000/docs> for interactive documentation.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/urls` | Create a short URL (`{"url": "https://..."}`) → `201` |
| `GET` | `/{code}` | Redirect to the original URL and record a click |
| `GET` | `/api/v1/urls/{code}/stats` | Click count and metadata |
| `DELETE` | `/api/v1/urls/{code}` | Delete (requires `X-API-Key` header) → `204` |
| `GET` | `/health` | Health check |

## Try it

```bash
curl -X POST http://127.0.0.1:8000/api/v1/urls \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.python.org"}'

curl -i http://127.0.0.1:8000/<short_code>
curl http://127.0.0.1:8000/api/v1/urls/<short_code>/stats
curl -X DELETE http://127.0.0.1:8000/api/v1/urls/<short_code> -H "X-API-Key: dev-secret-key"
```

## Configuration (environment variables)

| Variable | Default | Purpose |
|----------|---------|---------|
| `DB_PATH` | `shortener.db` | SQLite file location |
| `API_KEY` | `dev-secret-key` | Key required for deletes. **Change it in production** |

## Run tests

```bash
pytest
```

## Design notes

- **Validation:** Pydantic `AnyHttpUrl` rejects non-HTTP(S) schemes such as `javascript:`.
- **SQL injection:** all queries are parameterized.
- **Uniqueness:** `UNIQUE` constraint on `short_code` plus retry on collision.
- **Indexing:** the unique constraint indexes `short_code`; an index on `clicks.url_id` speeds up stats.
- **Caching:** `lru_cache` for hot code lookups (cleared on delete).
- **Rate limiting:** in-memory sliding window per IP → `429` with `Retry-After`.
- **Authorization:** API key compared in constant time.
- **Limitations:** the in-memory cache and rate limiter are per process. With multiple workers, use Redis.

## Stretch goals

Custom aliases, expiry dates, per-day analytics, PostgreSQL via SQLAlchemy, Redis cache and distributed rate limiting, queue-based click processing, Docker deployment.
