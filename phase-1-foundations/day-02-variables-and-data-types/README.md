# Day 02: Variables & Data Types

> **Phase 1 – Foundations** | Estimated time: 2 hours

## 🎯 Learning objectives

- Create and name variables correctly.
- Know the core built-in data types.
- Convert between types and read user input.
- Format output using f-strings.

## 📖 Concepts

### Variables

A variable is a name that refers to a value stored in memory.

```python
name = "Zaid"
age = 21
height = 5.9
is_student = True
```

Python is **dynamically typed**: you do not declare a type, and a name can later refer to a different type.

```python
x = 10
x = "ten"      # allowed, but avoid it in real code
```

### Naming rules and conventions

- Letters, digits, underscore; cannot start with a digit.
- Case-sensitive: `age` and `Age` differ.
- Cannot use keywords (`if`, `for`, `class`, …).
- Convention: `snake_case` for variables, `UPPER_CASE` for constants.

```python
user_name = "ali"
MAX_RETRIES = 3
```

### Core data types

| Type | Example | Notes |
|------|---------|-------|
| `int` | `42` | Unlimited size |
| `float` | `3.14` | Floating-point, can have precision errors |
| `str` | `"hi"` | Text, immutable |
| `bool` | `True`, `False` | Subclass of `int` |
| `NoneType` | `None` | Represents "no value" |

```python
print(type(42))        # <class 'int'>
print(0.1 + 0.2)       # 0.30000000000000004  (float precision)
print(isinstance(5, int))   # True
```

### Type conversion (casting)

```python
int("25")        # 25
float("3.5")     # 3.5
str(100)         # "100"
bool(0)          # False
bool("hello")    # True
int(7.9)         # 7  (truncates)
```

`int("abc")` raises `ValueError`. We handle that on Day 12.

### Taking input

`input()` always returns a **string**.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"{name} will be {age + 1} next year.")
```

### f-strings

```python
price = 49.5
print(f"Price: {price:.2f}")        # Price: 49.50
print(f"{1000000:,}")               # 1,000,000
print(f"{name!r}")                  # shows quotes, uses repr
print(f"{2 + 3 = }")                # 2 + 3 = 5 (debug format)
```

### Multiple assignment & swapping

```python
a, b, c = 1, 2, 3
x = y = 0
a, b = b, a          # swap without temp variable
```

### Everything is an object

```python
x = 5
print(id(x))         # memory identity
print(type(x))
```

## ⚠️ Common mistakes

- Forgetting to convert `input()` to `int` before arithmetic.
- Comparing floats with `==` (use `math.isclose`).
- Using names like `list`, `str`, or `sum` for variables, which hides built-ins.

## 🏋️ Exercises

1. Store your details in variables and print them with an f-string.
2. Ask for two numbers and print their sum, difference, product, and quotient.
3. Convert a temperature from Celsius to Fahrenheit: `F = C * 9/5 + 32`.
4. Swap two variables without using a third.
5. Print the type of: `10`, `10.0`, `"10"`, `True`, `None`.

## 🛠 Mini project: Simple bill calculator

Ask for the item price, quantity, and tax percentage. Print a formatted bill showing subtotal, tax, and total (2 decimal places).

## 📝 Summary

- Variables reference objects; Python is dynamically typed.
- Core types: `int`, `float`, `str`, `bool`, `None`.
- `input()` returns `str`; convert as needed.
- f-strings are the modern way to format output.

⬅️ [Day 01](../day-01-introduction/README.md) | ➡️ [Day 03 – Strings](../day-03-strings/README.md)
