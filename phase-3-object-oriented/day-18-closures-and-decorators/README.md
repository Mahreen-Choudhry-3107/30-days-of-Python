# Day 18: Closures & Decorators

> **Phase 3 – Object-Oriented Python** | Estimated time: 3 hours

## 🎯 Learning objectives

- Understand first-class functions and closures.
- Write decorators, with and without arguments.
- Preserve metadata using `functools.wraps`.
- Use common built-in decorators.

## 📖 Concepts

### First-class functions

Functions can be assigned to variables, passed as arguments, and returned.

```python
def shout(text): return text.upper()
f = shout
print(f("hi"))
```

### Closures

An inner function that remembers variables from its enclosing scope.

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
c(); c()          # 1, 2
```

### A decorator is a function that wraps another function

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow():
    sum(range(1_000_000))

slow()
```

`@timer` above `def slow()` is shorthand for `slow = timer(slow)`.

### Preserve metadata with `functools.wraps`

```python
from functools import wraps

def timer(func):
    @wraps(func)               # keeps __name__, __doc__
    def wrapper(*args, **kwargs):
        ...
        return func(*args, **kwargs)
    return wrapper
```

Always use `@wraps` in your decorators.

### Decorators with arguments

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello")
```

### Practical decorators

**Logging**

```python
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper
```

**Retry**

```python
import time

def retry(attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
```

**Authorization check**

```python
def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_admin"):
            raise PermissionError("Admins only")
        return func(user, *args, **kwargs)
    return wrapper
```

### Stacking decorators

```python
@log_calls
@timer
def work(): ...
# equivalent to work = log_calls(timer(work))
```

### Class-based decorators

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)
```

### Built-in and stdlib decorators

`@property`, `@staticmethod`, `@classmethod`, `@functools.lru_cache`, `@functools.cache`, `@functools.wraps`, `@dataclasses.dataclass`, `@abc.abstractmethod`.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

fib.cache_info()
```

## ⚠️ Common mistakes

- Forgetting `return` in the wrapper (the function returns `None`).
- Forgetting `@wraps`, which breaks introspection and debugging.
- Not forwarding `*args, **kwargs`.
- Confusing `@decorator` with `@decorator(args)`.

## 🏋️ Exercises

1. Write `@timer` and apply it to two functions.
2. Write `@validate_positive` that raises `ValueError` if any numeric argument is negative.
3. Write `@cache` manually using a dictionary.
4. Write `@retry(attempts=3)` and test it with a function that fails randomly.
5. Write `@rate_limit(calls=5, period=60)` using timestamps in a list.

## 🛠 Mini project: Function profiler

Build a `@profile` decorator that records the call count, total time, and average time of any function, and a `report()` function to print a sorted table.

## 📝 Summary

- Closures capture enclosing variables.
- Decorators wrap functions to add behavior without changing their code.
- Use `functools.wraps` and forward all arguments.

⬅️ [Day 17](../day-17-encapsulation-and-dunder-methods/README.md) | ➡️ [Day 19 – Context Managers, Dataclasses & Enums](../day-19-context-managers-dataclasses-enums/README.md)
