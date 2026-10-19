# Day 08: Functions

> **Phase 2 – Intermediate** | Estimated time: 2 hours

## 🎯 Learning objectives

- Define and call functions.
- Use parameters, default values, and keyword arguments.
- Return single and multiple values.
- Write docstrings and type hints.

## 📖 Concepts

### Why functions?

Functions give a name to a block of code so you can **reuse** it, **test** it, and keep programs **organized** (DRY: Don't Repeat Yourself).

### Defining and calling

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")
```

### Return values

```python
def add(a, b):
    return a + b

result = add(3, 4)      # 7
```

A function without `return` returns `None`. `return` ends the function immediately.

### Multiple return values (tuple)

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9])
```

### Parameters

```python
def power(base, exponent=2):          # default value
    return base ** exponent

power(3)                # 9
power(3, 3)             # 27 (positional)
power(exponent=4, base=2)   # 16 (keyword)
```

Rules: non-default parameters come before defaults; positional arguments before keyword arguments.

### The mutable default argument trap

```python
def add_item(item, items=[]):     # BAD: list created once
    items.append(item)
    return items

def add_item(item, items=None):   # GOOD
    if items is None:
        items = []
    items.append(item)
    return items
```

### Docstrings

```python
def area(radius):
    """Return the area of a circle.

    Args:
        radius: Radius of the circle (non-negative).

    Returns:
        The area as a float.
    """
    return 3.14159 * radius ** 2

help(area)
```

### Type hints

```python
def full_name(first: str, last: str) -> str:
    return f"{first} {last}"
```

Hints are not enforced at runtime, but editors and tools like `mypy` use them.

### Functions are objects

```python
def square(x): return x * x
operation = square
print(operation(5))        # 25
```

### Pure vs impure functions

A pure function depends only on its inputs and has no side effects (no printing, no modifying globals). Pure functions are easier to test.

## ⚠️ Common mistakes

- Printing inside a function instead of returning a value.
- Forgetting to call the function (`greet` vs `greet()`).
- Using mutable default arguments.
- Modifying a list argument unintentionally (lists are passed by object reference).

## 🏋️ Exercises

1. Write `is_even(n)` and `is_prime(n)`.
2. Write `factorial(n)` using a loop.
3. Write `count_vowels(text)`.
4. Write `average(numbers)` that returns `0` for an empty list.
5. Write `celsius_to_fahrenheit` and `fahrenheit_to_celsius`, each with docstrings and type hints.

## 🛠 Mini project: Calculator with functions

Create `add`, `subtract`, `multiply`, `divide` functions and a menu that calls them. Handle division by zero gracefully.

## 📝 Summary

- `def` defines a function; `return` sends a value back.
- Use default and keyword arguments carefully.
- Document with docstrings and add type hints.

⬅️ [Day 07](../../phase-1-foundations/day-07-dictionaries-and-sets/README.md) | ➡️ [Day 09 – Advanced Functions](../day-09-advanced-functions/README.md)
