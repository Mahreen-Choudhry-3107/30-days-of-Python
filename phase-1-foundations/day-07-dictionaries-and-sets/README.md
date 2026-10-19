# Day 07: Dictionaries & Sets (+ Week 1 Project)

> **Phase 1 – Foundations** | Estimated time: 3 hours

## 🎯 Learning objectives

- Store and retrieve data with dictionaries.
- Use sets for uniqueness and fast membership.
- Choose the right data structure.
- Complete your first project.

## 📖 Concepts

### Dictionaries

Key–value mappings. Keys must be hashable (str, int, tuple, …). Since Python 3.7 dictionaries preserve insertion order.

```python
student = {"name": "Ali", "age": 20, "marks": [80, 90]}
student["name"]            # 'Ali'
student["city"] = "Lahore" # add
student["age"] = 21        # update
del student["marks"]       # delete
```

### Safe access

```python
student.get("phone")               # None, no error
student.get("phone", "N/A")        # default value
"name" in student                  # True (checks keys)
```

`student["phone"]` raises `KeyError` if the key is missing.

### Iterating

```python
for key in student:                  # keys
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, value)
```

### Useful methods

```python
d = {"a": 1}
d.update({"b": 2, "c": 3})
d.pop("a")                   # remove and return
d.setdefault("z", 0)         # set only if missing
list(d.keys())
{**d, "x": 9}                # merge into new dict
d | {"y": 1}                 # merge (Python 3.9+)
```

### Counting with a dictionary

```python
text = "banana"
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print(count)       # {'b': 1, 'a': 3, 'n': 2}
```

(`collections.Counter` does this for you; see Day 10.)

### Nested dictionaries

```python
users = {
    "ali": {"age": 20, "skills": ["python", "sql"]},
    "sara": {"age": 22, "skills": ["java"]},
}
print(users["ali"]["skills"][0])    # python
```

### Sets

Unordered collections of **unique, hashable** elements with very fast membership checks.

```python
s = {1, 2, 3, 3}          # {1, 2, 3}
empty = set()             # {} creates an empty dict!
s.add(4); s.discard(1)
```

Set operations:

```python
a = {1, 2, 3}
b = {3, 4}
a | b      # union        {1,2,3,4}
a & b      # intersection {3}
a - b      # difference   {1,2}
a ^ b      # symmetric    {1,2,4}
a <= {1,2,3,4}   # subset
```

Removing duplicates: `unique = list(set(items))` (order is lost; use `dict.fromkeys(items)` to keep order).

### Choosing a structure

| Need | Use |
|------|-----|
| Ordered, changeable sequence | `list` |
| Fixed record | `tuple` |
| Lookup by key | `dict` |
| Uniqueness / membership | `set` |

## ⚠️ Common mistakes

- Using `{}` for an empty set.
- Accessing a missing key with `[]` instead of `.get()`.
- Using a list as a dictionary key (unhashable).
- Expecting sets to keep order.

## 🏋️ Exercises

1. Count the frequency of each word in a sentence.
2. Invert a dictionary (`{"a": 1}` → `{1: "a"}`).
3. Find common elements between two lists using sets.
4. Group names by their first letter into a dictionary of lists.
5. Merge two dictionaries; on duplicate keys, sum the values.

## 🛠 Week 1 Project: Number Guessing Game

Build a game where the computer picks a number and the player guesses with hints, attempt limits, and difficulty levels.

📁 Complete code: [`projects/project-01-number-guessing-game`](../../projects/project-01-number-guessing-game/README.md)

Try to build it yourself first, then compare.

## 📝 Summary

- Dictionaries map keys to values; use `.get()` for safe access.
- Sets store unique items and support math-style operations.
- Pick the structure that matches your access pattern.
- Week 1 complete: you can now write real programs.

⬅️ [Day 06](../day-06-lists-and-tuples/README.md) | ➡️ [Day 08 – Functions](../../phase-2-intermediate/day-08-functions/README.md)
