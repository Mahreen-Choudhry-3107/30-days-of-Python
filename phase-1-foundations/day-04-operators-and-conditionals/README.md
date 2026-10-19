# Day 04: Operators & Conditional Statements

> **Phase 1 – Foundations** | Estimated time: 2 hours

## 🎯 Learning objectives

- Use arithmetic, comparison, logical, and membership operators.
- Understand truthiness.
- Control program flow with `if`, `elif`, `else`, and `match`.

## 📖 Concepts

### Arithmetic operators

```python
10 + 3     # 13
10 - 3     # 7
10 * 3     # 30
10 / 3     # 3.333... (always float)
10 // 3    # 3   floor division
10 % 3     # 1   modulo (remainder)
2 ** 5     # 32  exponent
```

### Assignment operators

```python
x = 5
x += 2     # x = x + 2
x -= 1
x *= 3
x //= 2
```

### Comparison operators

`==`, `!=`, `>`, `<`, `>=`, `<=` return `True` or `False`. Chaining works:

```python
age = 25
print(18 <= age < 60)    # True
```

### Logical operators

```python
True and False    # False
True or False     # True
not True          # False
```

`and` / `or` use **short-circuit evaluation**: they stop as soon as the result is known.

### Identity and membership

```python
a = [1, 2]
b = [1, 2]
a == b          # True  (same value)
a is b          # False (different objects)
3 in [1, 2, 3]  # True
"x" not in "abc"  # True
```

Use `is` for `None` checks: `if value is None:`.

### Truthiness

Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`, `None`, `False`. Everything else is truthy.

```python
name = ""
if not name:
    print("Name is required")
```

### if / elif / else

```python
marks = 82

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

### Nested conditions

```python
age, has_id = 20, True
if age >= 18:
    if has_id:
        print("Entry allowed")
```

Prefer `if age >= 18 and has_id:` when it keeps code flatter.

### Ternary expression

```python
status = "adult" if age >= 18 else "minor"
```

### match-case (Python 3.10+)

```python
command = "stop"
match command:
    case "start":
        print("Starting")
    case "stop" | "halt":
        print("Stopping")
    case _:
        print("Unknown")
```

### Operator precedence (high to low)

`**` → unary `-` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`. Use parentheses for clarity.

## ⚠️ Common mistakes

- Using `=` instead of `==` in a condition.
- Forgetting the colon `:` after `if`/`elif`/`else`.
- Inconsistent indentation.
- Using `is` to compare numbers or strings.

## 🏋️ Exercises

1. Check whether a number is positive, negative, or zero.
2. Check whether a year is a leap year (divisible by 4, but not by 100 unless also by 400).
3. Find the largest of three numbers without using `max()`.
4. Build a grade calculator from marks.
5. Write a simple calculator that takes two numbers and an operator (`+ - * /`) using `match`.

## 🛠 Mini project: ATM menu simulator

Start with a balance of 5000. Show a menu (Check balance, Deposit, Withdraw, Exit) and respond to the user's choice. Reject withdrawals greater than the balance.

## 📝 Summary

- Operators: arithmetic, comparison, logical, identity, membership.
- Truthiness lets you write concise conditions.
- `if / elif / else` and `match` control the flow.

⬅️ [Day 03](../day-03-strings/README.md) | ➡️ [Day 05 – Loops](../day-05-loops/README.md)
