# Day 09: Advanced Functions

> **Phase 2 – Intermediate** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Accept flexible arguments with `*args` and `**kwargs`.
- Understand variable scope (LEGB).
- Use lambda functions and functional tools.
- Write recursive functions.

## 📖 Concepts

### `*args` and `**kwargs`

```python
def total(*numbers):            # tuple of positional args
    return sum(numbers)

total(1, 2, 3)                  # 6

def show(**info):               # dict of keyword args
    for k, v in info.items():
        print(k, v)

show(name="Ali", age=20)
```

Unpacking when calling:

```python
nums = [1, 2, 3]
total(*nums)
config = {"name": "Sara", "age": 22}
show(**config)
```

Argument order: `def f(a, b=1, *args, key=None, **kwargs)`.

### Keyword-only and positional-only

```python
def f(a, /, b, *, c):   # a positional-only, c keyword-only
    return a + b + c

f(1, 2, c=3)
```

### Scope: LEGB rule

Python looks up names in this order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "changed"
    inner()
    print(x)        # changed

def use_global():
    global counter
    counter += 1
```

Avoid `global` where possible; pass values in and return results instead.

### Lambda functions

Small anonymous functions with a single expression.

```python
square = lambda x: x * x
students = [("Ali", 80), ("Sara", 95)]
students.sort(key=lambda s: s[1], reverse=True)
```

### `map`, `filter`, `reduce`, `sorted`

```python
nums = [1, 2, 3, 4, 5]
list(map(lambda x: x * 2, nums))          # [2,4,6,8,10]
list(filter(lambda x: x % 2 == 0, nums))  # [2,4]

from functools import reduce
reduce(lambda a, b: a * b, nums)          # 120
```

List comprehensions (Day 13) are often more readable than `map`/`filter`.

### Higher-order functions

Functions that take or return functions.

```python
def apply(func, value):
    return func(value)

def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
double(10)          # 20
```

### Recursion

A function that calls itself. It needs a **base case** and progress toward it.

```python
def factorial(n):
    if n <= 1:           # base case
        return 1
    return n * factorial(n - 1)

def fib(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

Python limits recursion depth (default ~1000). For deep problems, use loops or `functools.lru_cache`.

### `functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

## ⚠️ Common mistakes

- Missing the base case in recursion (`RecursionError`).
- Overusing `global`.
- Writing long, unreadable lambdas.
- Confusing `*args` (tuple) with `**kwargs` (dict).

## 🏋️ Exercises

1. Write `multiply(*nums)` that multiplies any number of values.
2. Write a function `describe(**kwargs)` that prints a formatted profile.
3. Sort a list of dictionaries by a key using `lambda`.
4. Solve Tower of Hanoi recursively.
5. Flatten a nested list of arbitrary depth using recursion.

## 🛠 Mini project: Text analyzer

Write functions to count words, find the longest word, compute word frequencies (top N), and average word length. Use `*args`/`**kwargs` for optional filters like `min_length` and `ignore=[...]`.

## 📝 Summary

- `*args`/`**kwargs` provide flexible signatures.
- LEGB defines name lookup; use `nonlocal` and `global` sparingly.
- Lambdas, `map`, `filter`, and `sorted(key=...)` support functional style.
- Recursion needs a base case; memoization avoids repeated work.

⬅️ [Day 08](../day-08-functions/README.md) | ➡️ [Day 10 – Modules & Packages](../day-10-modules-and-packages/README.md)
