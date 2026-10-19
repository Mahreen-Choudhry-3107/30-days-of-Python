# Day 10: Modules, Packages & the Standard Library

> **Phase 2 – Intermediate** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Import and create modules and packages.
- Use important standard library modules.
- Install third-party packages with `pip`.
- Isolate projects with virtual environments.

## 📖 Concepts

### Modules

Any `.py` file is a module.

```python
import math
from math import sqrt, pi
import random as rnd
from math import *        # avoid: pollutes the namespace
```

### Creating your own module

`utils.py`:

```python
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    print(greet("test"))     # runs only when executed directly
```

`main.py`:

```python
import utils
print(utils.greet("Ali"))
```

`__name__ == "__main__"` is `True` only when the file is run directly, not when imported.

### Packages

A package is a folder of modules (with an `__init__.py` for regular packages).

```
shop/
├── __init__.py
├── cart.py
└── payment.py
```

```python
from shop.cart import add_item
from shop import payment
```

### Essential standard library modules

```python
import math
math.sqrt(16); math.ceil(2.1); math.floor(2.9); math.isclose(0.1 + 0.2, 0.3)

import random
random.randint(1, 10); random.choice(["a", "b"]); random.shuffle(lst); random.sample(lst, 2)

import datetime
now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M")

import os, sys
os.getcwd(); os.listdir("."); os.environ.get("HOME"); sys.argv

from pathlib import Path
Path("data") / "file.txt"; Path.cwd(); Path("a.txt").exists()

from collections import Counter, defaultdict, deque, namedtuple
Counter("banana").most_common(2)      # [('a', 3), ('n', 2)]
groups = defaultdict(list); groups["x"].append(1)

import itertools
list(itertools.permutations([1, 2, 3], 2))

import json, csv, time, statistics, uuid, secrets
statistics.mean([1, 2, 3, 4])
```

Tip: use `secrets` (not `random`) for passwords and tokens.

### pip and PyPI

```bash
pip install requests
pip install requests==2.32.0
pip uninstall requests
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Virtual environments

A virtual environment gives each project its own isolated packages.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install requests
deactivate
```

Never commit `.venv/` to Git. Commit `requirements.txt` instead.

### Import system basics

Python searches `sys.path` (current directory, installed packages, standard library). If you name your file `random.py`, `import random` will import **your file**.

## ⚠️ Common mistakes

- Naming files after standard modules (`random.py`, `json.py`).
- Installing packages globally instead of in a virtual environment.
- Circular imports (A imports B, B imports A).
- Using `from x import *`.

## 🏋️ Exercises

1. Create a `mathutils.py` module with `is_prime`, `gcd`, and `factorial`; import it elsewhere.
2. Use `collections.Counter` to find the three most common words in a paragraph.
3. Use `datetime` to calculate how many days remain until your next birthday.
4. Generate a secure random password using `secrets`.
5. Create a virtual environment, install `requests`, and freeze the requirements.

## 🛠 Mini project: Password generator package

Create a `passgen` package with modules `generator.py` (random password with options) and `strength.py` (score a password). Add a `main.py` that uses both.

## 📝 Summary

- Modules and packages organize code; `import` reuses it.
- The standard library is powerful; learn its main modules.
- Use `pip` and virtual environments for dependencies.

⬅️ [Day 09](../day-09-advanced-functions/README.md) | ➡️ [Day 11 – File Handling](../day-11-file-handling/README.md)
