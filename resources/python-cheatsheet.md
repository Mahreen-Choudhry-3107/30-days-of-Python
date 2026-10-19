# Python Cheat Sheet

## Data types
```python
int, float, str, bool, None
list [1, 2]     tuple (1, 2)     dict {"a": 1}     set {1, 2}
```

## Strings
```python
s.strip() s.split(",") ",".join(xs) s.replace(a, b) s.lower() s.startswith(x)
s[1:4]  s[::-1]  f"{x:.2f}"  f"{n:,}"  f"{name!r}"
```

## Lists / dicts / sets
```python
xs.append(x) xs.extend(ys) xs.pop() xs.sort(key=len) sorted(xs, reverse=True)
d.get(k, default) d.items() d.setdefault(k, v) d | other
a | b   a & b   a - b   a ^ b
```

## Control flow
```python
if x: ...  elif y: ...  else: ...
for i, v in enumerate(xs, 1): ...
for a, b in zip(xs, ys): ...
while cond: ...   break   continue
match value:
    case 1 | 2: ...
    case _: ...
```

## Functions
```python
def f(a, b=1, *args, key=None, **kwargs) -> int: ...
lambda x: x * 2
@decorator
```

## Comprehensions & generators
```python
[x * 2 for x in xs if x > 0]
{k: v for k, v in pairs}
{x for x in xs}
(x * x for x in xs)
def gen(): yield value
```

## Exceptions
```python
try: ...
except (ValueError, KeyError) as e: ...
else: ...
finally: ...
raise ValueError("message")
```

## Files
```python
with open("f.txt", encoding="utf-8") as f: data = f.read()
Path("a.txt").read_text()   json.load(f)   json.dump(obj, f, indent=2)
```

## Classes
```python
class A(Base):
    def __init__(self, x): super().__init__(); self.x = x
    def __repr__(self): return f"A({self.x})"
    @property
    def double(self): return self.x * 2
    @classmethod
    def make(cls): return cls(0)
    @staticmethod
    def util(): ...

@dataclass
class P: x: int; y: int = 0
```

## Useful standard library
`collections.Counter / defaultdict / deque` · `itertools` · `functools.lru_cache` · `pathlib` · `datetime` · `json` · `csv` · `re` · `logging` · `argparse` · `sqlite3` · `subprocess` · `threading` · `asyncio` · `secrets` · `dataclasses` · `enum`

## Commands
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip freeze > requirements.txt
pytest -v
python -m pdb script.py
```
