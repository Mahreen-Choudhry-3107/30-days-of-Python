# Day 20: Regular Expressions & Date/Time

> **Phase 3 – Object-Oriented Python** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Search, validate, and extract text with `re`.
- Work with dates, times, durations, and formatting.

## 📖 Concepts

## Part 1: Regular expressions

### Basics

```python
import re

text = "Contact: ali@example.com, sara@test.org"
re.search(r"\w+@\w+\.\w+", text)         # first match (Match object or None)
re.findall(r"\w+@\w+\.\w+", text)        # list of all matches
re.sub(r"\d", "#", "Call 123")           # replace
re.split(r"[,;]\s*", "a, b;c")           # split
re.fullmatch(r"\d{4}", "2024")           # entire string must match
```

Always write patterns as **raw strings** (`r"..."`).

### Pattern cheat sheet

| Pattern | Meaning |
|---------|---------|
| `.` | any character except newline |
| `\d` `\w` `\s` | digit, word char, whitespace |
| `\D` `\W` `\S` | negations |
| `^` `$` | start / end |
| `*` `+` `?` | 0+, 1+, 0 or 1 |
| `{n}` `{n,m}` | exact / range repetition |
| `[abc]` `[^abc]` | character class / negated |
| `(...)` | capture group |
| `(?:...)` | non-capturing group |
| `a\|b` | alternation |
| `\b` | word boundary |

### Groups

```python
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2025-03-14")
m.group(0)      # whole match
m.group(1)      # '2025'
m.groups()      # ('2025', '03', '14')

m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2025-03")
m.group("year")
m.groupdict()
```

### Compiling and flags

```python
pattern = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", re.IGNORECASE)
pattern.match("test@example.com")

re.findall(r"^\w+", text, re.MULTILINE)
```

### Greedy vs lazy

```python
re.findall(r"<.+>", "<a><b>")      # ['<a><b>']   greedy
re.findall(r"<.+?>", "<a><b>")     # ['<a>', '<b>']  lazy
```

### Practical examples

```python
# phone numbers
re.findall(r"\b03\d{2}-\d{7}\b", text)

# log line
line = '192.168.1.1 - - [10/Oct/2025:13:55:36] "GET /index.html" 200'
re.search(r'(?P<ip>[\d.]+).*"(?P<method>\w+) (?P<path>\S+)" (?P<status>\d{3})', line).groupdict()
```

Regex is powerful but not for everything: do not parse HTML or validate complex formats (like full email standards) with it. Use proper parsers.

## Part 2: Date and time

### `datetime` basics

```python
from datetime import datetime, date, time, timedelta, timezone

now = datetime.now()
today = date.today()
d = date(2025, 3, 14)
dt = datetime(2025, 3, 14, 18, 30)
```

### Formatting and parsing

```python
now.strftime("%Y-%m-%d %H:%M:%S")       # to string
datetime.strptime("14/03/2025", "%d/%m/%Y")   # from string
now.isoformat()
datetime.fromisoformat("2025-03-14T18:30:00")
```

Common codes: `%Y` year, `%m` month, `%d` day, `%H` 24-hour, `%I` 12-hour, `%M` minute, `%S` second, `%A` weekday name, `%B` month name.

### Arithmetic

```python
tomorrow = today + timedelta(days=1)
diff = date(2025, 12, 31) - today
print(diff.days)

delta = timedelta(hours=2, minutes=30)
delta.total_seconds()
```

### Time zones

```python
from zoneinfo import ZoneInfo        # Python 3.9+

utc_now = datetime.now(timezone.utc)
karachi = utc_now.astimezone(ZoneInfo("Asia/Karachi"))
```

Best practice: **store and compute in UTC**, convert to local time only for display. Avoid naive datetimes (no timezone) in systems used across regions.

### Useful helpers

```python
import calendar
calendar.monthrange(2025, 2)         # (weekday of first day, number of days)
today.weekday()                      # Monday = 0
today.isocalendar()
```

## ⚠️ Common mistakes

- Forgetting raw strings in regex patterns.
- Using `re.match` when you meant `re.search` (`match` anchors at the start).
- Greedy patterns matching too much.
- Mixing naive and aware datetimes (raises `TypeError`).
- Using `datetime.utcnow()` (deprecated); prefer `datetime.now(timezone.utc)`.

## 🏋️ Exercises

1. Validate a Pakistani mobile number format such as `03XX-XXXXXXX`.
2. Extract all hashtags and mentions from a tweet-like string.
3. Parse an Apache-style log line into a dictionary.
4. Calculate the exact age (years, months, days) from a birth date.
5. Convert a meeting time from UTC to three different time zones.

## 🛠 Mini project: Birthday & deadline reminder

Read a list of `(name, date)` entries; print how many days are left for each upcoming event, sorted by nearest date, and highlight events happening within 7 days. Add a regex-based input validator for the `YYYY-MM-DD` format.

## 📝 Summary

- `re` finds, validates, extracts, and replaces text patterns.
- `datetime` handles dates, times, arithmetic, and formatting.
- Work in UTC internally and convert for display.

⬅️ [Day 19](../day-19-context-managers-dataclasses-enums/README.md) | ➡️ [Day 21 – Review & Library System](../day-21-review-and-library-system/README.md)
