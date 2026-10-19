# Day 25: HTTP APIs & Web Scraping

> **Phase 4 – Advanced & Professional** | Estimated time: 3 hours

## 🎯 Learning objectives

- Call REST APIs using `requests`.
- Handle status codes, timeouts, and retries.
- Scrape simple pages responsibly with BeautifulSoup.

## 📖 Concepts

### HTTP refresher

A request has a **method**, **URL**, **headers**, and optional **body**. A response has a **status code**, **headers**, and **body**. Common status codes: `200` OK, `201` Created, `400` Bad Request, `401` Unauthorized, `403` Forbidden, `404` Not Found, `429` Too Many Requests, `500` Server Error.

### `requests` basics

```bash
pip install requests
```

```python
import requests

r = requests.get("https://api.github.com/users/octocat", timeout=10)
print(r.status_code)
print(r.headers["Content-Type"])
data = r.json()                 # parsed JSON
print(data["login"])
```

**Always set a `timeout`.** `requests` has no default timeout and can hang forever.

### Query parameters, headers, POST

```python
r = requests.get(
    "https://httpbin.org/get",
    params={"q": "python", "page": 2},
    headers={"User-Agent": "learning-bot/1.0"},
    timeout=10,
)

r = requests.post("https://httpbin.org/post", json={"name": "Ali"}, timeout=10)
r = requests.post(url, data={"field": "value"}, timeout=10)     # form data
r = requests.put(url, json=payload, timeout=10)
r = requests.delete(url, timeout=10)
```

### Error handling

```python
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()            # raises HTTPError for 4xx/5xx
    data = r.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Network problem:", e)
except ValueError:
    print("Response was not valid JSON")
```

### Sessions and retries

```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retry))

session.headers.update({"Authorization": f"Bearer {token}"})
r = session.get(url, timeout=10)
```

Use **exponential backoff** for retries and only retry idempotent requests unless you use idempotency keys.

### Authentication

- API keys in headers or query parameters (prefer headers).
- Bearer tokens: `Authorization: Bearer <token>`.
- Keep secrets in **environment variables**, never in source code:

```python
import os
API_KEY = os.environ["WEATHER_API_KEY"]
```

### Pagination

```python
def fetch_all(url):
    results = []
    while url:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        payload = r.json()
        results.extend(payload["items"])
        url = payload.get("next")
    return results
```

### Web scraping

```bash
pip install beautifulsoup4
```

```python
import requests
from bs4 import BeautifulSoup

html = requests.get("https://example.com", timeout=10).text
soup = BeautifulSoup(html, "html.parser")

soup.title.text
soup.find("h1").get_text(strip=True)
for link in soup.find_all("a", href=True):
    print(link["href"], link.text)

for item in soup.select("div.product > h2.title"):    # CSS selectors
    print(item.get_text(strip=True))
```

### Scraping ethics and legality

- Check the site's **terms of service** and `robots.txt`.
- Prefer an official **API** over scraping.
- Rate-limit your requests (`time.sleep`), identify your bot, cache results.
- Do not scrape personal data or bypass access controls.
- Dynamic pages built with JavaScript may need a browser tool (Playwright/Selenium) or the underlying JSON API.

### Saving results

```python
import csv, json

with open("items.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)
```

## ⚠️ Common mistakes

- No timeout on requests.
- Ignoring status codes and assuming `.json()` always works.
- Hard-coding API keys in code or committing them to Git.
- Scraping too fast and getting blocked.
- Fragile selectors tied to page layout.

## 🏋️ Exercises

1. Fetch a GitHub user's public repos and list the 5 most-starred.
2. Build a function with retry and exponential backoff around `requests.get`.
3. Call a public API with pagination and combine all pages.
4. Scrape headlines from a site that permits scraping and save them to CSV.
5. Write a small client class `WeatherClient` with methods, error handling, and a session.

## 🛠 Mini project: Quotes scraper & analyzer

Scrape the practice site `https://quotes.toscrape.com` (built for scraping practice) across multiple pages, store quotes in SQLite, and report the most common authors and tags.

## 📝 Summary

- `requests` calls APIs; always use timeouts, status checks, and error handling.
- Keep secrets out of code.
- Scrape politely and prefer official APIs.

⬅️ [Day 24](../day-24-databases-with-sqlite/README.md) | ➡️ [Day 26 – REST API with FastAPI](../day-26-rest-api-with-fastapi/README.md)
