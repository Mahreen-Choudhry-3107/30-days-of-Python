# Day 30: Capstone Project & Next Steps

> **Phase 4 – Advanced & Professional** | Estimated time: 5+ hours

## 🎯 Learning objectives

- Combine everything you learned into one production-style project.
- Plan your next learning steps.

## 🏆 Capstone: URL Shortener API

Build a REST API that shortens URLs, redirects visitors, and tracks clicks. This is the same project blueprint suggested in the backend handbook, so you can implement those concepts in Python.

### Requirements

| Feature | Concepts practiced |
|---------|-------------------|
| `POST /api/v1/urls` creates a short link | REST, validation (Pydantic), status codes |
| `GET /{code}` redirects to the original URL | HTTP redirects, database lookups, indexing |
| `GET /api/v1/urls/{code}/stats` shows click count | SQL, aggregation |
| `DELETE /api/v1/urls/{code}` deletes a link | API keys / authorization |
| Reject invalid or unsafe URLs | Input validation, security |
| Unique short codes | Uniqueness constraints, retry on collision |
| Rate-limit creation | Rate limiting |
| Cache hot lookups | Caching (`lru_cache` or a dictionary with TTL) |
| Automated tests | pytest, `TestClient` |

### Suggested steps

1. Design the database schema (`urls`, `clicks`) and add indexes.
2. Write the repository layer using parameterized SQL.
3. Write the API with Pydantic models and proper status codes.
4. Add validation, rate limiting, and API-key protection for delete.
5. Add tests (happy paths and error cases).
6. Add logging and a `/health` endpoint.
7. Write the README and package it.

📁 Complete reference solution: [`projects/project-06-url-shortener-api`](../../projects/project-06-url-shortener-api/README.md)

Try to build it first. Compare with the reference only after you finish.

### Stretch goals

- Custom aliases and expiry dates.
- Click analytics by day and by referrer.
- Replace SQLite with PostgreSQL via SQLAlchemy.
- Use Redis for caching and distributed rate limiting.
- Process click events asynchronously with a queue.
- Dockerize the app and deploy it (Render, Railway, Fly.io, or a VPS).

## 🔁 Final self-assessment

Rate yourself 1–5 on each area; revisit anything below 4.

- [ ] Data types, strings, collections
- [ ] Control flow and functions
- [ ] Modules, packages, virtual environments
- [ ] Files, JSON, CSV
- [ ] Exceptions
- [ ] Comprehensions, iterators, generators
- [ ] OOP: classes, inheritance, dunder methods
- [ ] Decorators, context managers, dataclasses
- [ ] Testing and logging
- [ ] Concurrency basics
- [ ] SQL with Python
- [ ] HTTP APIs and scraping
- [ ] Building REST APIs
- [ ] Data analysis basics
- [ ] CLI tools
- [ ] Clean code and packaging

## 🧭 Where to go next

Pick **one** direction and build projects in it:

| Path | Learn next | Project ideas |
|------|-----------|---------------|
| **Backend development** | FastAPI/Django, PostgreSQL, Redis, Docker, auth (JWT/OAuth2), message queues | E-commerce API, blog platform, booking system |
| **Data science / analytics** | pandas in depth, SQL, statistics, scikit-learn, visualization | Sales dashboard, churn prediction |
| **Machine learning / AI** | NumPy, scikit-learn, PyTorch, LLM APIs | Classifier, recommender, RAG chatbot |
| **Automation / DevOps** | Bash, Docker, GitHub Actions, cloud basics, Ansible | Deployment scripts, monitoring tool |
| **Web scraping & data engineering** | Playwright, Scrapy, Airflow, data warehousing | Price tracker, ETL pipeline |

### Advice for continued growth

1. **Build projects** every week; tutorials alone do not stick.
2. **Read other people's code** on GitHub.
3. Learn **data structures & algorithms** (practice on LeetCode, HackerRank, or Advent of Code).
4. Contribute to **open source**; start with documentation and small fixes.
5. Learn **Git, Linux, SQL, and Docker**: they matter in every Python career.
6. Keep a public **portfolio**: 3–5 well-documented repositories beat 30 unfinished ones.
7. Teach what you learn: write posts, explain concepts to others.

## 🎓 Congratulations

You have completed 30 Days of Python. You can now design, build, test, and package real programs. Keep building.

⬅️ [Day 29](../day-29-best-practices-and-packaging/README.md) | 🏠 [Back to main README](../../README.md)
