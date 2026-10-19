# Day 21: Week 3 Review + Library Management System

> **Phase 3 – Object-Oriented Python** | Estimated time: 4 hours

## 🎯 Learning objectives

- Consolidate Days 15–20.
- Design a small multi-class system with clear responsibilities.

## 🔁 Week 3 recap

| Day | Topic | Key takeaway |
|-----|-------|--------------|
| 15 | Classes & objects | State + behavior in one unit |
| 16 | Inheritance & polymorphism | Reuse code, program to behavior |
| 17 | Encapsulation & dunder methods | Properties and Pythonic objects |
| 18 | Closures & decorators | Wrap behavior without editing functions |
| 19 | Context managers, dataclasses, enums | Cleaner, safer code |
| 20 | Regex & datetime | Text patterns and time handling |

## ✅ Self-check questions

1. What is the difference between `__str__` and `__repr__`?
2. When would you choose composition over inheritance?
3. What does `@functools.wraps` do?
4. Why is `tags: list = []` problematic in a dataclass?
5. What does `with` call on an object?
6. What is the difference between greedy and lazy regex quantifiers?

## 🛠 Project: Library Management System

### Requirements

- Books with ISBN, title, author, and availability.
- Members who can borrow up to 3 books at a time.
- Borrow and return with due dates (14 days) and late-fee calculation.
- Custom exceptions for invalid operations (book unavailable, limit reached, unknown ISBN/member).
- Search by title or author.
- A report of overdue books.

### Design hint

| Class | Responsibility |
|-------|----------------|
| `Book` (dataclass) | Stores book data |
| `Member` | Tracks borrowed books |
| `Loan` (dataclass) | Links a book, a member, and dates |
| `Library` | Coordinates everything; owns the collections |

📁 Complete code: [`projects/project-03-library-management`](../../projects/project-03-library-management/README.md)

### Stretch goals

- Persist data in JSON, then in SQLite (Day 24).
- Add reservations and waiting lists.
- Add unit tests (Day 22).

## 📝 Summary

You can now design programs using classes, enums, dataclasses, decorators, and custom exceptions. Next: professional practices such as testing, concurrency, databases, and web APIs.

⬅️ [Day 20](../day-20-regex-and-datetime/README.md) | ➡️ [Day 22 – Testing, Debugging & Logging](../../phase-4-advanced/day-22-testing-debugging-logging/README.md)
