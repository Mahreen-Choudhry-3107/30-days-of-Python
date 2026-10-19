# Project 02: Expense Tracker

**Week 2 project** | Difficulty: ⭐⭐

A menu-driven command-line expense tracker with JSON persistence.

## Features

- Add, list, filter, summarize, and delete expenses.
- Data stored in `expenses.json` (created automatically).
- Validation for amounts, categories, and dates.
- Safe handling of a missing or corrupted data file.

## Run

```bash
python main.py
```

## Concepts used

Functions, type hints, `pathlib`, JSON, exceptions, comprehensions, `defaultdict`, `datetime`.

## Extension ideas

- Export to CSV.
- Monthly report and budget alerts.
- Turn the menu into subcommands using `argparse` (Day 28).
- Rewrite storage with SQLite (Day 24).
