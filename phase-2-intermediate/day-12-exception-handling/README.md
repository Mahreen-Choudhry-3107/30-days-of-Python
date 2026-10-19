# Day 12: Exception Handling

> **Phase 2 – Intermediate** | Estimated time: 2 hours

## 🎯 Learning objectives

- Catch and handle errors with `try` / `except`.
- Use `else`, `finally`, and `raise`.
- Create custom exceptions.
- Read tracebacks and debug.

## 📖 Concepts

### Errors vs exceptions

- **Syntax errors** are caught before the program runs.
- **Exceptions** occur at runtime and can be handled.

Common exceptions: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`, `AttributeError`, `ImportError`.

### try / except

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number.")
```

### Multiple exceptions

```python
try:
    result = 10 / int(input("Divide by: "))
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, KeyError) as e:
    print("Other error:", e)
```

### else and finally

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
else:
    print("Opened successfully")     # runs only if no exception
    f.close()
finally:
    print("Always runs")             # cleanup code
```

### Catching broadly

```python
try:
    risky()
except Exception as e:                # not bare `except:`
    print(f"Unexpected: {e!r}")
    raise                              # re-raise after logging
```

Avoid bare `except:`; it hides `KeyboardInterrupt` and real bugs. Catch the **most specific** exception you can handle.

### Raising exceptions

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

### Custom exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Balance {balance} is less than {amount}")
        self.balance = balance
        self.amount = amount

raise InsufficientFundsError(100, 500)
```

### Exception chaining

```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Config is invalid") from e
```

### EAFP vs LBYL

- **LBYL** (Look Before You Leap): `if key in d: value = d[key]`
- **EAFP** (Easier to Ask Forgiveness than Permission): `try: value = d[key] except KeyError: ...`

Python commonly prefers EAFP, but use whichever is clearer.

### assert

```python
assert age >= 0, "Age cannot be negative"
```

Use `assert` for internal sanity checks, **not** to validate user input (assertions can be disabled with `-O`).

### Reading a traceback

Read from the **bottom up**: the last line is the exception type and message, the lines above show where it happened.

```
Traceback (most recent call last):
  File "app.py", line 8, in <module>
    divide(5, 0)
  File "app.py", line 3, in divide
    return a / b
ZeroDivisionError: division by zero
```

## ⚠️ Common mistakes

- Bare `except:` or `except Exception: pass` (silent failures).
- Wrapping too much code in a single `try` block.
- Using exceptions for normal control flow in hot paths.
- Forgetting to re-raise after logging when the caller must know.

## 🏋️ Exercises

1. Write `safe_int(text, default=0)` that never crashes.
2. Write a safe division function returning `None` on error.
3. Keep asking for a valid positive integer until the user enters one.
4. Create a custom `InvalidEmailError` and a validator that raises it.
5. Read a file safely, handling missing files and permission errors differently.

## 🛠 Mini project: Robust bank account

Create `deposit`, `withdraw`, and `transfer` functions with custom exceptions (`InsufficientFundsError`, `InvalidAmountError`). Show friendly messages for each case.

## 📝 Summary

- Handle specific exceptions with `try` / `except`; use `else` and `finally` appropriately.
- `raise` signals errors; custom exceptions make intent clear.
- Never silently swallow exceptions.

⬅️ [Day 11](../day-11-file-handling/README.md) | ➡️ [Day 13 – Comprehensions & Generators](../day-13-comprehensions-and-generators/README.md)
