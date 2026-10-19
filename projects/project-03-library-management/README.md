# Project 03: Library Management System

**Week 3 project** | Difficulty: ⭐⭐⭐

An object-oriented library system: books, members, loans, due dates, and late fees.

## Run the demo

```bash
python library.py
```

## Run the tests

```bash
pip install pytest
pytest
```

## Design

| Class | Role |
|-------|------|
| `Book` | dataclass for book data |
| `Loan` | dataclass linking a book with due date; computes late fees |
| `Member` | borrower with a loan limit |
| `Library` | service class coordinating all operations |
| `LibraryError` family | custom exceptions for each failure case |

## Concepts used

Classes, dataclasses, composition, custom exceptions, `datetime`, comprehensions, type hints, pytest.

## Extension ideas

- JSON or SQLite persistence.
- Reservation queue.
- Command-line interface with `argparse`.
