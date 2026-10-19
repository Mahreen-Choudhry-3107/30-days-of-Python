# Day 13: Comprehensions, Iterators & Generators

> **Phase 2 – Intermediate** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Write list, dict, and set comprehensions.
- Understand iterables vs iterators.
- Build generators with `yield` for memory-efficient code.

## 📖 Concepts

### List comprehensions

```python
squares = [x ** 2 for x in range(1, 6)]            # [1,4,9,16,25]
evens = [x for x in range(20) if x % 2 == 0]
labels = ["even" if x % 2 == 0 else "odd" for x in range(4)]
pairs = [(x, y) for x in range(2) for y in range(2)]
flat = [n for row in [[1, 2], [3, 4]] for n in row]
```

Structure: `[expression for item in iterable if condition]`.

### Dict and set comprehensions

```python
word_len = {w: len(w) for w in ["apple", "kiwi"]}
unique_lengths = {len(w) for w in ["apple", "kiwi", "pear"]}
inverted = {v: k for k, v in word_len.items()}
```

### When not to use them

If a comprehension needs multiple nested loops or complicated conditions, use a normal loop for readability.

### Iterables and iterators

- **Iterable:** something you can loop over (has `__iter__`): list, str, dict, file.
- **Iterator:** an object that produces values one at a time (`__next__`).

```python
it = iter([10, 20])
next(it)     # 10
next(it)     # 20
next(it)     # StopIteration
```

A `for` loop calls `iter()` once and `next()` repeatedly until `StopIteration`.

### Custom iterator

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

list(Countdown(3))   # [3, 2, 1]
```

### Generators

Functions with `yield` produce values lazily and remember their state.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)
```

```python
def read_large_file(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()
```

Generators let you process huge data with constant memory.

### Generator expressions

```python
total = sum(x * x for x in range(1_000_000))     # no list is built
```

Use `()` instead of `[]`.

### `yield from` and itertools

```python
def chain(*iterables):
    for it in iterables:
        yield from it

import itertools
itertools.islice(itertools.count(1), 5)      # 1,2,3,4,5
itertools.chain([1, 2], [3, 4])
itertools.groupby(sorted(data), key=...)
```

### Infinite generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
list(islice(fibonacci(), 10))
```

### Comparison

| | List | Generator |
|---|------|-----------|
| Memory | All items stored | One item at a time |
| Reusable | Yes | Single pass |
| Indexing | Yes | No |

## ⚠️ Common mistakes

- Trying to reuse an exhausted generator.
- Building huge lists when a generator would do.
- Over-nesting comprehensions, which hurts readability.
- Using a comprehension only for side effects (e.g. `[print(x) for x in xs]`).

## 🏋️ Exercises

1. Create a list of the squares of all odd numbers from 1 to 20.
2. Build a dictionary mapping each word in a sentence to its length.
3. Flatten a 2D list with a comprehension.
4. Write a generator that yields prime numbers indefinitely.
5. Write a generator that reads a file and yields only lines containing a keyword.

## 🛠 Mini project: Log line filter

Use a generator pipeline: read lines → filter lines containing `ERROR` → extract timestamps → count. Each step is a generator, so memory use stays constant.

## 📝 Summary

- Comprehensions create collections concisely.
- Iterators produce values via `__next__`; generators create them with `yield`.
- Generators are lazy and memory-efficient.

⬅️ [Day 12](../day-12-exception-handling/README.md) | ➡️ [Day 14 – Review & Expense Tracker](../day-14-review-and-expense-tracker/README.md)
