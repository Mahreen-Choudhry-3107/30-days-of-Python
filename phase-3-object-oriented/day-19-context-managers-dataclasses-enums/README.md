# Day 19: Context Managers, Dataclasses, Enums & Type Hints

> **Phase 3 – Object-Oriented Python** | Estimated time: 3 hours

## 🎯 Learning objectives

- Build your own context managers.
- Reduce boilerplate with dataclasses.
- Model fixed choices with enums.
- Use type hints effectively.

## 📖 Concepts

### Context managers

Objects that set up and tear down a resource around a `with` block.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.3f}s")
        return False          # do not suppress exceptions

with Timer():
    sum(range(1_000_000))
```

### `contextlib.contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def open_db(path):
    conn = connect(path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
```

Other helpers: `contextlib.suppress(FileNotFoundError)`, `contextlib.redirect_stdout`, `contextlib.ExitStack`.

### Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)

p = Product("Pen", 1.5)
print(p)                       # Product(name='Pen', price=1.5, tags=[])
p == Product("Pen", 1.5)       # True (auto __eq__)
```

Options:

```python
@dataclass(frozen=True, order=True)       # immutable and sortable
class Version:
    major: int
    minor: int = 0

@dataclass
class Order:
    id: int
    items: list = field(default_factory=list)

    def __post_init__(self):             # validation after init
        if self.id <= 0:
            raise ValueError("id must be positive")
```

Helpers: `dataclasses.asdict(obj)`, `dataclasses.replace(obj, price=2)`.

Never use a mutable default like `tags: list = []`; use `field(default_factory=list)`.

### Enums

```python
from enum import Enum, auto

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    CLOSED = "closed"

s = Status.ACTIVE
s.name         # 'ACTIVE'
s.value        # 'active'
Status("closed")           # Status.CLOSED
for item in Status:
    print(item)

class Color(Enum):
    RED = auto()
    GREEN = auto()
```

Enums prevent typos and "magic strings". Variants: `IntEnum`, `Flag`, `StrEnum` (3.11+).

### Type hints

```python
def greet(name: str, times: int = 1) -> str: ...

ages: dict[str, int] = {"ali": 20}
maybe: str | None = None            # Python 3.10+
numbers: list[int] = []
```

Useful tools from `typing`:

```python
from typing import Callable, Iterable, Optional, TypedDict, Protocol, Literal, Any

def apply(fn: Callable[[int], int], xs: Iterable[int]) -> list[int]:
    return [fn(x) for x in xs]

Mode = Literal["r", "w"]

class User(TypedDict):
    name: str
    age: int

class Drawable(Protocol):
    def draw(self) -> None: ...
```

Check types statically with `mypy` or `pyright`. Hints are not enforced at runtime.

## ⚠️ Common mistakes

- Forgetting `return False` / not handling exceptions in `__exit__` properly.
- Using mutable defaults in dataclasses.
- Comparing enum members by value strings instead of members.
- Believing type hints validate input at runtime (they do not).

## 🏋️ Exercises

1. Write a context manager that temporarily changes the working directory.
2. Create a `@dataclass` `Employee` with validation in `__post_init__`.
3. Create an `OrderStatus` enum and a function that returns the allowed next statuses.
4. Add full type hints to your earlier Expense Tracker functions.
5. Create a frozen dataclass `Point` and use it as a dictionary key.

## 🛠 Mini project: Task manager model

Model tasks with a `Priority` enum, a `Status` enum, and a `Task` dataclass. Add helper functions to filter and sort tasks and a context manager that autosaves changes to JSON.

## 📝 Summary

- Context managers guarantee cleanup.
- Dataclasses remove boilerplate for data-holding classes.
- Enums define named constants safely.
- Type hints document and help verify code.

⬅️ [Day 18](../day-18-closures-and-decorators/README.md) | ➡️ [Day 20 – Regex & Datetime](../day-20-regex-and-datetime/README.md)
