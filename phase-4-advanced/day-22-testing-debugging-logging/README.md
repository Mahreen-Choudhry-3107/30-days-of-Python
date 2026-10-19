# Day 22: Testing, Debugging & Logging

> **Phase 4 – Advanced & Professional** | Estimated time: 3 hours

## 🎯 Learning objectives

- Write automated tests with `pytest`.
- Use fixtures, parametrization, and mocking.
- Debug with `pdb` and tracebacks.
- Replace `print()` debugging with the `logging` module.

## 📖 Concepts

### Why test?

Tests catch regressions, document behavior, and make refactoring safe. A good test is **fast, isolated, repeatable, and readable**.

### Your first pytest test

`calculator.py`:

```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b
```

`test_calculator.py`:

```python
import pytest
from calculator import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

Run:

```bash
pip install pytest
pytest            # discover and run all tests
pytest -v         # verbose
pytest -k add     # run tests matching a name
pytest -x         # stop at first failure
```

Naming: files `test_*.py`, functions `test_*`.

### Parametrized tests

```python
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected
```

### Fixtures

```python
@pytest.fixture
def sample_user():
    return {"name": "Ali", "age": 20}

def test_user_name(sample_user):
    assert sample_user["name"] == "Ali"

@pytest.fixture
def temp_file(tmp_path):                 # built-in tmp_path fixture
    f = tmp_path / "data.txt"
    f.write_text("hello")
    return f
```

### Mocking

Replace slow or external dependencies (network, time, database) with fakes.

```python
from unittest.mock import patch, Mock

def get_status(url):
    import requests
    return requests.get(url, timeout=5).status_code

def test_get_status():
    with patch("requests.get") as fake_get:
        fake_get.return_value = Mock(status_code=200)
        assert get_status("http://x") == 200
        fake_get.assert_called_once()
```

pytest also has `monkeypatch` for patching attributes and environment variables.

### Test structure: Arrange – Act – Assert

```python
def test_withdraw_reduces_balance():
    account = BankAccount(100)       # arrange
    account.withdraw(30)             # act
    assert account.balance == 70     # assert
```

### Coverage

```bash
pip install pytest-cov
pytest --cov=. --cov-report=term-missing
```

Coverage shows which lines ran; high coverage does not guarantee good tests.

### Debugging

**Tracebacks:** read from the bottom.

**`breakpoint()`** drops into `pdb`:

```python
def compute(x):
    breakpoint()
    return x * 2
```

| pdb command | Action |
|-------------|--------|
| `n` | next line |
| `s` | step into |
| `c` | continue |
| `p var` | print value |
| `l` | list source |
| `q` | quit |

VS Code and PyCharm also provide graphical debuggers with breakpoints and watches.

### Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

logger.debug("Detailed info")
logger.info("User %s logged in", "ali")
logger.warning("Disk almost full")
logger.error("Payment failed")
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")   # includes traceback
```

Levels: `DEBUG < INFO < WARNING < ERROR < CRITICAL`.

Write to a file with rotation:

```python
from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=3)
logging.getLogger().addHandler(handler)
```

**Never log secrets** (passwords, tokens, full card numbers).

### Test-Driven Development (TDD)

1. Write a failing test.
2. Write the minimum code to pass it.
3. Refactor.

## ⚠️ Common mistakes

- Tests that depend on each other or on execution order.
- Testing implementation details instead of behavior.
- Mocking too much so tests prove nothing.
- Using `print()` for diagnostics in production code.

## 🏋️ Exercises

1. Write tests for `is_palindrome` including edge cases (empty string, mixed case).
2. Parametrize tests for a `grade(marks)` function.
3. Add tests for your Expense Tracker's `summarize` and `add_expense` functions.
4. Mock a function that calls an external API and test both success and failure.
5. Add logging with levels to your Library Management project.

## 🛠 Mini project: Test suite for a shopping cart

Write a `Cart` class (add, remove, total, apply_discount) with a complete pytest suite using fixtures and parametrization, and aim for 90%+ coverage.

## 📝 Summary

- pytest makes tests short and expressive; use fixtures and parametrization.
- Mock external dependencies.
- Use `breakpoint()` and logging instead of scattered prints.

⬅️ [Day 21](../../phase-3-object-oriented/day-21-review-and-library-system/README.md) | ➡️ [Day 23 – Concurrency](../day-23-concurrency/README.md)
