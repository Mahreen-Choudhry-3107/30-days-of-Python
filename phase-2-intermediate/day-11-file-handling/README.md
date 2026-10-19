# Day 11: File Handling (Text, CSV, JSON)

> **Phase 2 – Intermediate** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Read and write text files safely.
- Work with paths using `pathlib`.
- Read and write CSV and JSON data.

## 📖 Concepts

### Opening files

```python
f = open("notes.txt", "r", encoding="utf-8")
data = f.read()
f.close()
```

Always prefer the context manager, which closes the file automatically, even on errors:

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    data = f.read()
```

### File modes

| Mode | Meaning |
|------|---------|
| `r` | read (default); error if missing |
| `w` | write; **overwrites** existing content |
| `a` | append to the end |
| `x` | create; error if it exists |
| `b` | binary (e.g. `rb`, `wb`) |
| `+` | read and write |

### Reading

```python
with open("notes.txt", encoding="utf-8") as f:
    all_text = f.read()           # entire file as a string

with open("notes.txt", encoding="utf-8") as f:
    lines = f.readlines()         # list of lines

with open("notes.txt", encoding="utf-8") as f:
    for line in f:                # best for large files
        print(line.strip())
```

### Writing

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.writelines(["Line 2\n", "Line 3\n"])

with open("out.txt", "a", encoding="utf-8") as f:
    f.write("Appended\n")
```

### `pathlib`

```python
from pathlib import Path

p = Path("data") / "users.txt"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hello", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
print(p.exists(), p.suffix, p.stem, p.name)

for file in Path(".").glob("*.py"):
    print(file)
```

### CSV

```python
import csv

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "marks"])
    writer.writerow(["Ali", 90])

with open("students.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):          # rows as dictionaries
        print(row["name"], row["marks"])
```

### JSON

```python
import json

data = {"name": "Ali", "skills": ["python", "sql"]}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("data.json", encoding="utf-8") as f:
    loaded = json.load(f)

text = json.dumps(data)          # dict -> JSON string
obj = json.loads(text)           # JSON string -> dict
```

JSON supports: object, array, string, number, boolean, null. Python tuples become arrays; sets are not supported.

### Handling missing files

```python
from pathlib import Path
if Path("data.json").exists():
    ...
```

Better (Day 12): wrap in `try/except FileNotFoundError`.

### Binary files

```python
with open("photo.jpg", "rb") as src, open("copy.jpg", "wb") as dst:
    dst.write(src.read())
```

## ⚠️ Common mistakes

- Using `"w"` on a file you meant to append to (data loss).
- Forgetting `encoding="utf-8"`, which causes issues on Windows.
- Forgetting `newline=""` when writing CSV (blank lines on Windows).
- Not stripping `\n` from lines.

## 🏋️ Exercises

1. Count lines, words, and characters in a text file.
2. Copy a file to a new name, converting it to uppercase.
3. Read a CSV of marks and write a new CSV containing only students above 60.
4. Save a dictionary to JSON and load it back.
5. Write a script that lists all `.py` files in a folder recursively using `pathlib`.

## 🛠 Mini project: Persistent to-do list

A command-line to-do app that stores tasks in `tasks.json`: add, list, complete, and delete tasks. Tasks must survive restarts.

## 📝 Summary

- Use `with open(...)` and specify the encoding.
- `pathlib` makes path handling clean and portable.
- `csv` and `json` handle the most common data formats.

⬅️ [Day 10](../day-10-modules-and-packages/README.md) | ➡️ [Day 12 – Exception Handling](../day-12-exception-handling/README.md)
