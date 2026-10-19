# Day 29: Best Practices, Performance & Packaging

> **Phase 4 – Advanced & Professional** | Estimated time: 3 hours

## 🎯 Learning objectives

- Write clean, idiomatic, maintainable Python.
- Use linters, formatters, and type checkers.
- Profile and optimize responsibly.
- Structure and package a project; use Git effectively.
- Apply basic security practices.

## 📖 Concepts

### PEP 8 and idiomatic Python

- 4-space indentation, lines ≤ 88–100 characters.
- `snake_case` functions/variables, `PascalCase` classes, `UPPER_CASE` constants.
- Meaningful names (`user_count`, not `uc`).
- Prefer:

```python
# Pythonic                         # Less Pythonic
for i, x in enumerate(items):      for i in range(len(items)):
if not items:                      if len(items) == 0:
with open(p) as f:                 f = open(p) ... f.close()
", ".join(names)                   loop with +=
x = d.get("k", default)            if "k" in d: ... else: ...
```

- Follow **The Zen of Python**: `import this`.

### Clean code principles

- **Single responsibility:** one function does one thing.
- **DRY:** extract repeated logic, but do not abstract too early.
- **Small functions**, shallow nesting, early returns:

```python
def process(user):
    if user is None:
        return None
    if not user.active:
        return None
    return user.name
```

- Comments explain **why**, not **what**. Keep docstrings current.
- Avoid magic numbers; use named constants or enums.
- Prefer composition and pure functions where possible.

### Tooling

```bash
pip install ruff mypy black pre-commit
ruff check .          # fast linter
ruff format .         # or: black .
mypy .                # static type checking
```

Set up **pre-commit** hooks so formatting and linting run before every commit.

### Project structure

```
myproject/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
└── tests/
    └── test_core.py
```

### `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "myproject"
version = "0.1.0"
description = "Short description"
requires-python = ">=3.10"
dependencies = ["requests>=2.31"]

[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]

[project.scripts]
myproject = "myproject.cli:main"

[tool.setuptools.packages.find]
where = ["src"]
```

Install for development: `pip install -e ".[dev]"`. Build: `pip install build && python -m build`.

### Configuration and secrets

- Read configuration from **environment variables**.
- Keep `.env` out of version control; provide `.env.example`.
- Pin dependency versions (`requirements.txt` or a lock file) for reproducible builds.
- Run `pip-audit` to check for vulnerable dependencies.

### Security checklist

- Never use `eval()` / `exec()` on untrusted input.
- Use parameterized SQL queries.
- Hash passwords with `bcrypt`/`argon2`, never MD5/SHA1 or plain text.
- Use the `secrets` module for tokens.
- Avoid `pickle.load` on untrusted data.
- Validate and sanitize all external input.
- Do not log secrets.

### Performance

> Measure first. Premature optimization wastes time.

```python
import timeit
timeit.timeit("sum(range(1000))", number=10_000)

import cProfile, pstats
cProfile.run("main()", "profile.out")
pstats.Stats("profile.out").sort_stats("cumtime").print_stats(10)
```

Practical wins:

- Choose the right data structure (`set`/`dict` lookups are O(1) vs O(n) for lists).
- Use generators for large data.
- Cache expensive pure functions with `functools.lru_cache`.
- Use `"".join()` for building large strings.
- Use vectorized NumPy/pandas operations.
- Reduce I/O and database round trips (batching, indexes).
- Use `collections.deque` for queues, `heapq` for priority queues, `bisect` for sorted lists.

Complexity cheat sheet: list `append` O(1), list `insert(0)` O(n), `x in list` O(n), `x in set/dict` O(1), `sort` O(n log n).

### Git workflow essentials

```bash
git init
git status
git add .
git commit -m "feat: add expense summary"
git switch -c feature/summary
git push -u origin feature/summary
```

- Commit small, meaningful changes with clear messages (e.g. Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
- Use branches and pull requests; review code.
- Maintain a good `README.md`, `.gitignore`, and license.

### Documentation

Write a README that covers: what the project does, installation, usage examples, configuration, how to run tests, and contribution guidelines.

### Common design patterns in Python

| Pattern | Pythonic form |
|---------|---------------|
| Strategy | pass a function as an argument |
| Singleton | a module-level object |
| Factory | a function or classmethod returning instances |
| Observer | callbacks or signals |
| Decorator | `@decorator` syntax |
| Context manager | `with` statement |
| Repository | class wrapping data access |

## ⚠️ Common mistakes

- Giant functions and deeply nested logic.
- Optimizing without measuring.
- Committing secrets, virtual environments, or `__pycache__`.
- No tests, no README, no pinned dependencies.

## 🏋️ Exercises

1. Refactor one of your earlier projects: smaller functions, better names, type hints, docstrings.
2. Run `ruff` and `mypy` on a project and fix all reported issues.
3. Convert one project into an installable package with `pyproject.toml` and a console script.
4. Profile a slow function, optimize it, and show before/after timings.
5. Write a complete README for your best project.

## 🛠 Mini project: Ship a package

Take your Log Analyzer (or another project), structure it under `src/`, add tests, linting, type hints, a `pyproject.toml`, and a CI-ready `README.md`. Install it in a fresh virtual environment to verify it works.

## 📝 Summary

- Readable, tested, typed code is professional code.
- Use linters, formatters, and type checkers automatically.
- Profile before optimizing; package and document your work.

⬅️ [Day 28](../day-28-cli-tools-and-automation/README.md) | ➡️ [Day 30 – Capstone & Next Steps](../day-30-capstone-and-next-steps/README.md)
