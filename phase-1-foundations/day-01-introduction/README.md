# Day 01: Introduction to Python

> **Phase 1 – Foundations** | Estimated time: 1.5 hours

## 🎯 Learning objectives

- Understand what Python is and where it is used.
- Install Python and run code in the REPL and from a file.
- Write your first programs using `print()`.
- Use comments and understand indentation.

## 📖 Concepts

### What is Python?

Python is a high-level, interpreted, general-purpose language known for readable syntax. It is used for web backends, automation, data science, machine learning, scripting, testing, and more.

**Why learn it?** Simple syntax, huge standard library, a large ecosystem (PyPI), and strong job demand.

### Installing Python

1. Download Python 3.10 or newer from [python.org](https://www.python.org/downloads/).
2. On Windows, tick **"Add Python to PATH"** during installation.
3. Verify:

```bash
python --version      # or python3 --version
```

Recommended editor: VS Code with the Python extension (or PyCharm).

### Two ways to run Python

**1. REPL (interactive shell)** – type `python` and try things out:

```python
>>> 2 + 3
5
>>> print("Hello")
Hello
```

**2. Script file** – save code in `hello.py` and run:

```bash
python hello.py
```

### Your first program

```python
print("Hello, World!")
```

### `print()` in detail

```python
print("Hello", "Python")                 # Hello Python
print("a", "b", "c", sep="-")            # a-b-c
print("Loading", end="...")              # no newline at the end
print("done")                            # Loading...done
print("Line 1\nLine 2")                  # \n = new line
print("Tab\tseparated")                  # \t = tab
```

### Comments

```python
# This is a single-line comment
x = 10  # inline comment

"""
This is a multi-line string, often used
as a block comment or docstring.
"""
```

### Indentation

Python uses indentation (4 spaces by convention) instead of braces to define blocks. You will use this from Day 4 onwards.

```python
if True:
    print("Indented correctly")
```

### How Python runs your code

Source (`.py`) → compiled to bytecode → executed by the Python Virtual Machine (CPython). Code runs **top to bottom**, line by line.

## ⚠️ Common mistakes

- Using `Print()` instead of `print()` – Python is **case-sensitive**.
- Forgetting quotes around text: `print(Hello)` → `NameError`.
- Mixing tabs and spaces for indentation.
- Naming your file `random.py` or `math.py`, which can shadow standard modules.

## 🏋️ Exercises

1. Print your name, city, and favorite language, each on its own line.
2. Print `Python*is*fun` using the `sep` argument.
3. Print a 3-line pattern using `\n`:
   ```
   *
   **
   ***
   ```
4. Add comments to explain each line of your program.
5. Open the REPL and calculate `15 * 4 + 7`, `2 ** 10`, and `17 // 5`.

## 🛠 Mini project: Personal intro card

Write `intro.py` that prints a neatly formatted card:

```
==============================
 Name   : Your Name
 Role   : Python Learner
 Goal   : Finish 30 Days of Python
==============================
```

## 📝 Summary

- Python is readable, versatile, and beginner friendly.
- Run code via REPL or `python file.py`.
- `print()` outputs text; `#` starts a comment.
- Indentation defines blocks.

➡️ **Next:** [Day 02 – Variables & Data Types](../day-02-variables-and-data-types/README.md)
