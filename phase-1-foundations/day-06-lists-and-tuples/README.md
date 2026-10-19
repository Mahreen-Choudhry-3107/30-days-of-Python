# Day 06: Lists & Tuples

> **Phase 1 – Foundations** | Estimated time: 2 hours

## 🎯 Learning objectives

- Create and modify lists.
- Use list methods, slicing, and sorting.
- Understand shallow vs deep copying.
- Use tuples and unpacking.

## 📖 Concepts

### Lists

Ordered, **mutable** collections that can hold mixed types.

```python
nums = [10, 20, 30]
mixed = [1, "two", 3.0, [4, 5]]
empty = []
```

### Access and slicing

```python
nums[0]        # 10
nums[-1]       # 30
nums[1:]       # [20, 30]
nums[::-1]     # reversed copy
```

### Modifying lists

```python
nums.append(40)            # add at end
nums.insert(1, 15)         # insert at index
nums.extend([50, 60])      # add many
nums.remove(15)            # remove first match
last = nums.pop()          # remove and return last
del nums[0]                # delete by index
nums[0] = 99               # assign
```

### Useful methods and functions

```python
nums = [3, 1, 2]
len(nums); sum(nums); min(nums); max(nums)
nums.sort()                # in place
nums.sort(reverse=True)
sorted(nums)               # returns a new list
nums.reverse()
nums.index(2)              # position of value
nums.count(2)
2 in nums                  # membership
```

Sorting with a key:

```python
words = ["banana", "kiwi", "apple"]
words.sort(key=len)        # by length
```

### Copying lists

```python
a = [1, 2, 3]
b = a            # same object! changes affect both
c = a.copy()     # shallow copy (also a[:] or list(a))

import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)   # fully independent
```

### Nested lists (matrix)

```python
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])        # 6
for row in matrix:
    print(row)
```

### Tuples

Ordered, **immutable** sequences.

```python
point = (3, 4)
single = (5,)              # trailing comma required
x, y = point               # unpacking
first, *rest = (1, 2, 3, 4)   # first=1, rest=[2,3,4]
```

**Use tuples** for fixed data (coordinates, RGB, return values). Tuples can be dictionary keys; lists cannot.

### List vs Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Mutable | Yes | No |
| Syntax | `[]` | `()` |
| Use | Changing collections | Fixed records |
| Hashable | No | Yes (if contents are) |

### Performance note

`x in list` is O(n). If you check membership often, use a `set` (Day 07).

## ⚠️ Common mistakes

- `b = a` does not copy a list.
- `nums = nums.sort()` sets `nums` to `None` because `sort()` returns `None`.
- Modifying a list while iterating over it.
- `[[0] * 3] * 3` creates three references to the same inner list. Use `[[0] * 3 for _ in range(3)]`.

## 🏋️ Exercises

1. Find the second largest number in a list.
2. Remove duplicates from a list while preserving order.
3. Rotate a list by `k` positions.
4. Transpose a 2×3 matrix.
5. Given a list of tuples `(name, marks)`, sort by marks descending.

## 🛠 Mini project: Student marks manager

Store student names and marks in lists. Show the average, topmost scorer, and students above average. Allow adding and removing students from a menu.

## 📝 Summary

- Lists are mutable; tuples are immutable.
- Know slicing, `append`, `extend`, `pop`, `sort`, `sorted`.
- Copying lists needs care; `=` only creates another reference.

⬅️ [Day 05](../day-05-loops/README.md) | ➡️ [Day 07 – Dictionaries & Sets](../day-07-dictionaries-and-sets/README.md)
