# Python Interview Questions

## Basics
1. **What is the difference between a list and a tuple?** Lists are mutable; tuples are immutable and hashable (if their contents are).
2. **What is the difference between `==` and `is`?** `==` compares values; `is` compares object identity.
3. **What are mutable and immutable types?** Mutable: list, dict, set. Immutable: int, float, str, tuple, frozenset, bool.
4. **What is the difference between `/`, `//`, and `%`?** True division, floor division, and remainder.
5. **What is truthiness?** Empty containers, zero, `None`, and `False` are falsy; most other values are truthy.

## Functions
6. **What are `*args` and `**kwargs`?** Collect extra positional arguments (tuple) and keyword arguments (dict).
7. **Why are mutable default arguments dangerous?** The default is created once at definition time and shared across calls.
8. **Explain LEGB.** Local, Enclosing, Global, Built-in name lookup order.
9. **What is a closure?** An inner function that remembers variables from its enclosing scope.
10. **What is a decorator?** A callable that takes a function and returns a (usually wrapped) function.

## Data structures & iteration
11. **List comprehension vs generator expression?** The list is built in memory at once; the generator produces values lazily.
12. **What is the difference between an iterable and an iterator?** An iterable can produce an iterator via `iter()`; an iterator implements `__next__`.
13. **How does a dictionary work internally?** A hash table; keys must be hashable; average O(1) lookup.
14. **Shallow copy vs deep copy?** Shallow copies the container only; deep copies nested objects recursively.

## OOP
15. **What are dunder methods?** Special methods like `__init__`, `__str__`, `__eq__` that integrate objects with Python syntax.
16. **`__str__` vs `__repr__`?** `__str__` is for users; `__repr__` is unambiguous for developers.
17. **What is MRO?** Method Resolution Order, the order in which base classes are searched (C3 linearization).
18. **`@staticmethod` vs `@classmethod`?** A static method gets no automatic first argument; a class method gets the class (`cls`).
19. **Inheritance vs composition?** "is-a" vs "has-a"; prefer composition when "is-a" does not hold.
20. **What is duck typing?** Behavior matters more than declared type.

## Advanced
21. **What is the GIL?** A lock in CPython allowing one thread to execute Python bytecode at a time; limits CPU-bound threading.
22. **Threads vs processes vs asyncio?** Threads/async for I/O-bound work; processes for CPU-bound work.
23. **What are context managers?** Objects implementing `__enter__`/`__exit__` used with `with` for guaranteed cleanup.
24. **What is a generator and why use it?** A function using `yield`; lazy and memory-efficient.
25. **How does Python manage memory?** Reference counting plus a cyclic garbage collector.
26. **What are type hints?** Optional annotations used by tools (mypy) and editors; not enforced at runtime.

## Practical
27. **How do you handle configuration and secrets?** Environment variables or a secret manager; never commit them.
28. **How do you prevent SQL injection in Python?** Use parameterized queries or ORM APIs.
29. **How do you structure and test a project?** `src/` layout, `pytest`, fixtures, linting, type checking, CI.
30. **How would you speed up slow code?** Profile first, then improve the algorithm/data structure, cache, vectorize, reduce I/O, or add concurrency/multiprocessing as appropriate.

## Coding problems to practice
- Reverse a string / check palindrome
- Two-sum, anagram check, first non-repeating character
- FizzBuzz, Fibonacci (iterative, recursive, memoized)
- Flatten nested list
- Count word frequency
- Merge two sorted lists
- Implement an LRU cache
- Validate balanced brackets
- Binary search
- Group anagrams
