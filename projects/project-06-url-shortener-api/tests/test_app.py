import importlib
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("DB_PATH", str(tmp_path / "test.db"))
    monkeypatch.setenv("API_KEY", "test-key")
    import app as app_module
    app_module = importlib.reload(app_module)
    app_module.init_db()
    app_module._cached_lookup.cache_clear()
    with TestClient(app_module.app) as c:
        yield c, app_module


def test_create_and_redirect_and_stats(client):
    c, _ = client
    r = c.post("/api/v1/urls", json={"url": "https://example.com/page"})
    assert r.status_code == 201
    code = r.json()["short_code"]

    redirect = c.get(f"/{code}", follow_redirects=False)
    assert redirect.status_code == 307
    assert redirect.headers["location"] == "https://example.com/page"

    c.get(f"/{code}", follow_redirects=False)
    stats = c.get(f"/api/v1/urls/{code}/stats").json()
    assert stats["clicks"] == 2


def test_invalid_url_rejected(client):
    c, _ = client
    assert c.post("/api/v1/urls", json={"url": "not-a-url"}).status_code == 422
    assert c.post("/api/v1/urls", json={"url": "javascript:alert(1)"}).status_code == 422


def test_unknown_code_404(client):
    c, _ = client
    assert c.get("/doesnotexist", follow_redirects=False).status_code == 404
    assert c.get("/api/v1/urls/doesnotexist/stats").status_code == 404


def test_delete_requires_api_key(client):
    c, _ = client
    code = c.post("/api/v1/urls", json={"url": "https://example.com"}).json()["short_code"]
    assert c.delete(f"/api/v1/urls/{code}").status_code == 401
    assert c.delete(f"/api/v1/urls/{code}", headers={"x-api-key": "test-key"}).status_code == 204
    assert c.get(f"/{code}", follow_redirects=False).status_code == 404


def test_rate_limit(client):
    c, app_module = client
    app_module._hits.clear()
    statuses = [c.post("/api/v1/urls", json={"url": "https://example.com"}).status_code
                for _ in range(app_module.RATE_LIMIT + 2)]
    assert statuses[:app_module.RATE_LIMIT] == [201] * app_module.RATE_LIMIT
    assert statuses[-1] == 429
