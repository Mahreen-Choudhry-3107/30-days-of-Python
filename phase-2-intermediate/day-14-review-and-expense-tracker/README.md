# Day 14: Week 2 Review + Expense Tracker Project

> **Phase 2 – Intermediate** | Estimated time: 3–4 hours

## 🎯 Learning objectives

- Consolidate Days 8–13.
- Combine functions, modules, files, exceptions, and comprehensions in a real project.

## 🔁 Week 2 recap

| Day | Topic | Key takeaway |
|-----|-------|--------------|
| 08 | Functions | Reusable blocks with parameters and return values |
| 09 | Advanced functions | `*args`, `**kwargs`, scope, lambda, recursion |
| 10 | Modules & packages | `import`, stdlib, `pip`, virtual environments |
| 11 | File handling | `with open`, `pathlib`, CSV, JSON |
| 12 | Exceptions | `try/except/else/finally`, `raise`, custom errors |
| 13 | Comprehensions & generators | Concise, lazy data processing |

## ✅ Self-check questions

1. What is the difference between `*args` and `**kwargs`?
2. Why is `def f(x, items=[])` dangerous?
3. What does `with open(...)` guarantee?
4. When would you use `finally`?
5. What is the difference between a list comprehension and a generator expression?
6. What does `if __name__ == "__main__":` do?

## 🛠 Project: Expense Tracker (CLI)

A command-line app that stores expenses in a JSON file.

### Requirements

- Add an expense (amount, category, description, date).
- List all expenses, optionally filtered by category.
- Show a summary with totals per category and the overall total.
- Delete an expense by ID.
- Data persists between runs.
- Input validation and graceful error handling.

📁 Complete code: [`projects/project-02-expense-tracker`](../../projects/project-02-expense-tracker/README.md)

### How to approach it

1. Plan the data structure (list of dictionaries).
2. Write storage functions (`load_expenses`, `save_expenses`).
3. Write the feature functions (add, list, summary, delete).
4. Build the menu loop.
5. Add validation and exception handling.

### Stretch goals

- Export to CSV.
- Monthly reports using `datetime`.
- Budget limits per category with warnings.

## 📝 Summary

You can now write structured, multi-function programs that persist data and handle errors. Next you will learn to model the real world with classes.

⬅️ [Day 13](../day-13-comprehensions-and-generators/README.md) | ➡️ [Day 15 – Classes & Objects](../../phase-3-object-oriented/day-15-classes-and-objects/README.md)
