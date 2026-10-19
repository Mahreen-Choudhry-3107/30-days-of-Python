# Day 17: Encapsulation, Properties & Dunder Methods

> **Phase 3 – Object-Oriented Python** | Estimated time: 3 hours

## 🎯 Learning objectives

- Control access to attributes using naming conventions and properties.
- Implement special ("dunder") methods to make objects feel built-in.
- Use `@classmethod` and `@staticmethod`.

## 📖 Concepts

### Encapsulation

Hide internal details and expose a clean interface. Python relies on convention rather than strict access control:

| Name | Meaning |
|------|---------|
| `name` | public |
| `_name` | "internal use" by convention |
| `__name` | name-mangled to `_Class__name` (discourages accidental override) |

### Properties

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius          # uses the setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):               # read-only computed property
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
t.celsius = 30
print(t.fahrenheit)
```

Properties let you start with a public attribute and add validation later **without changing the interface**.

### Dunder (magic) methods

| Method | Triggered by |
|--------|--------------|
| `__str__` | `str(obj)`, `print(obj)` – user-friendly |
| `__repr__` | `repr(obj)`, debugger – unambiguous |
| `__eq__` | `a == b` |
| `__lt__`, `__le__`, … | comparisons, sorting |
| `__add__`, `__sub__`, `__mul__` | `+`, `-`, `*` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[i]` |
| `__contains__` | `x in obj` |
| `__iter__`, `__next__` | iteration |
| `__bool__` | truthiness |
| `__call__` | `obj()` |
| `__hash__` | hashing (sets, dict keys) |

### Example: a Vector class

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

v = Vector(1, 2) + Vector(3, 4)     # Vector(4, 6)
print(abs(Vector(3, 4)))             # 5.0
```

If you define `__eq__`, define `__hash__` too if the object should be hashable.

### Container-like class

```python
class Playlist:
    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        return self._songs[index]

    def __iter__(self):
        return iter(self._songs)

    def __contains__(self, song):
        return song in self._songs
```

### `@classmethod` and `@staticmethod`

```python
class User:
    def __init__(self, name, age):
        self.name, self.age = name, age

    @classmethod
    def from_string(cls, text):          # alternative constructor
        name, age = text.split(",")
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):                   # utility, no self/cls
        return age >= 18

u = User.from_string("Ali,22")
User.is_adult(u.age)
```

### `__slots__` (optional optimization)

```python
class Point:
    __slots__ = ("x", "y")      # no per-instance __dict__, saves memory
```

### `functools.total_ordering`

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, n): self.n = n
    def __eq__(self, o): return self.n == o.n
    def __lt__(self, o): return self.n < o.n
```

## ⚠️ Common mistakes

- Returning non-strings from `__str__`.
- Defining `__eq__` without `__hash__` and then using objects in sets.
- Using `__name` expecting true privacy (it is only mangled).
- Putting heavy logic in property getters that look like cheap attribute access.

## 🏋️ Exercises

1. Add a validated `age` property to a `Person` class (0–120).
2. Implement a `Fraction` class with `+`, `-`, `*`, `==`, and `__str__`.
3. Implement `Money` with currency checking in `__add__`.
4. Make a `Deck` class of cards supporting `len()`, indexing, and iteration.
5. Add an alternative constructor `from_dict` to a class of your choice.

## 🛠 Mini project: Matrix class

Implement a `Matrix` class with `__add__`, `__mul__` (matrix and scalar), `__eq__`, `__repr__`, and a `transpose()` method.

## 📝 Summary

- Encapsulation uses conventions (`_name`) and `@property`.
- Dunder methods let your classes work with Python syntax.
- `@classmethod` makes alternative constructors; `@staticmethod` groups utilities.

⬅️ [Day 16](../day-16-inheritance-and-polymorphism/README.md) | ➡️ [Day 18 – Closures & Decorators](../day-18-closures-and-decorators/README.md)
