"""Expense Tracker - Week 2 project.

Concepts used: functions, JSON file storage, pathlib, exception handling,
comprehensions, collections.defaultdict, and input validation.
"""

import json
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


# ---------- storage ----------
def load_expenses() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Warning: data file is corrupted. Starting with an empty list.")
        return []


def save_expenses(expenses: list[dict]) -> None:
    DATA_FILE.write_text(json.dumps(expenses, indent=2), encoding="utf-8")


def next_id(expenses: list[dict]) -> int:
    return max((e["id"] for e in expenses), default=0) + 1


# ---------- features ----------
def add_expense(expenses: list[dict], amount: float, category: str,
                description: str = "", when: str | None = None) -> dict:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if not category.strip():
        raise ValueError("Category cannot be empty.")
    when = when or date.today().isoformat()
    datetime.strptime(when, "%Y-%m-%d")  # raises ValueError if invalid

    expense = {
        "id": next_id(expenses),
        "amount": round(amount, 2),
        "category": category.strip().lower(),
        "description": description.strip(),
        "date": when,
    }
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def filter_expenses(expenses: list[dict], category: str | None = None) -> list[dict]:
    if category is None:
        return expenses
    return [e for e in expenses if e["category"] == category.strip().lower()]


def summarize(expenses: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]
    return dict(totals)


def delete_expense(expenses: list[dict], expense_id: int) -> bool:
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            del expenses[i]
            save_expenses(expenses)
            return True
    return False


# ---------- presentation ----------
def print_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<4} {'Date':<11} {'Category':<12} {'Amount':>10}  Description")
    print("-" * 60)
    for e in expenses:
        print(f"{e['id']:<4} {e['date']:<11} {e['category']:<12} "
              f"{e['amount']:>10.2f}  {e['description']}")


def print_summary(expenses: list[dict]) -> None:
    totals = summarize(expenses)
    if not totals:
        print("No expenses yet.")
        return
    print("\nCategory totals")
    print("-" * 28)
    for category, total in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
        print(f"{category:<15} {total:>10.2f}")
    print("-" * 28)
    print(f"{'TOTAL':<15} {sum(totals.values()):>10.2f}")


# ---------- menu ----------
MENU = """
==== Expense Tracker ====
1. Add expense
2. List expenses
3. List by category
4. Summary
5. Delete expense
6. Exit
"""


def prompt_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    expenses = load_expenses()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                amount = prompt_float("Amount: ")
                category = input("Category: ")
                description = input("Description (optional): ")
                when = input("Date YYYY-MM-DD (blank = today): ").strip() or None
                e = add_expense(expenses, amount, category, description, when)
                print(f"Added expense #{e['id']}.")
            elif choice == "2":
                print_expenses(expenses)
            elif choice == "3":
                category = input("Category: ")
                print_expenses(filter_expenses(expenses, category))
            elif choice == "4":
                print_summary(expenses)
            elif choice == "5":
                expense_id = int(input("Expense ID to delete: "))
                print("Deleted." if delete_expense(expenses, expense_id) else "ID not found.")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except ValueError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
