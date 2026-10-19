# Day 03: Strings

> **Phase 1 – Foundations** | Estimated time: 2 hours

## 🎯 Learning objectives

- Create strings in different ways.
- Use indexing and slicing.
- Apply common string methods.
- Understand immutability.

## 📖 Concepts

### Creating strings

```python
a = 'single'
b = "double"
c = """multi
line"""
path = r"C:\new\table"      # raw string: backslashes are literal
```

### Indexing and slicing

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
#   -6 -5 -4 -3 -2 -1

print(s[0])        # P
print(s[-1])       # n
print(s[1:4])      # yth
print(s[:3])       # Pyt
print(s[3:])       # hon
print(s[::2])      # Pto  (step 2)
print(s[::-1])     # nohtyP  (reverse)
```

Slice syntax: `s[start:stop:step]` (stop is exclusive).

### Immutability

```python
s = "hello"
# s[0] = "H"      # TypeError: strings cannot be changed
s = "H" + s[1:]   # create a new string instead
```

### Common methods

```python
text = "  Hello, Python World  "

text.strip()              # remove surrounding whitespace
text.lower(), text.upper()
text.title()              # Hello, Python World
text.replace("Python", "Java")
text.find("Python")       # index or -1
text.count("o")
text.startswith("  He"), text.endswith("  ")
"a,b,c".split(",")        # ['a', 'b', 'c']
"-".join(["a", "b", "c"]) # 'a-b-c'
"42".isdigit(), "abc".isalpha(), "abc123".isalnum()
"hi".center(10, "*")      # ****hi****
"7".zfill(3)              # 007
```

### Operations

```python
"Hi" + " there"       # concatenation
"ab" * 3              # ababab
"py" in "python"      # True
len("python")         # 6
```

### Formatting

```python
name, score = "Ali", 92.456
print(f"{name:>10}")          # right-align in width 10
print(f"{score:.1f}")         # 92.5
print("{} scored {}".format(name, score))
```

### Escape characters

| Escape | Meaning |
|--------|---------|
| `\n` | newline |
| `\t` | tab |
| `\\` | backslash |
| `\"` | double quote |

### Unicode

Python 3 strings are Unicode: `"سلام"`, `"こんにちは"`, and emojis all work. `ord("A")` gives 65 and `chr(65)` gives `"A"`.

### Building strings efficiently

Prefer `"".join(parts)` over repeated `+` inside large loops.

## ⚠️ Common mistakes

- Trying to modify a string in place.
- Off-by-one errors in slicing (the stop index is excluded).
- Forgetting that `split()` returns a list, not a string.
- Calling methods without parentheses: `s.upper` vs `s.upper()`.

## 🏋️ Exercises

1. Reverse a string using slicing.
2. Check whether a string is a palindrome (ignore case and spaces).
3. Count vowels in a sentence.
4. Convert `"hello world from python"` to title case without `.title()`.
5. Given `"  john.doe@example.com "`, clean it and extract the username and domain.

## 🛠 Mini project: Username generator

Ask for first name, last name, and birth year. Generate a username like `jdoe_1999` (first letter + last name, lowercase, underscore, year).

## 📝 Summary

- Strings are immutable sequences of characters.
- Slicing: `s[start:stop:step]`.
- Many useful methods: `strip`, `split`, `join`, `replace`, `find`.
- Use f-strings for formatting.

⬅️ [Day 02](../day-02-variables-and-data-types/README.md) | ➡️ [Day 04 – Operators & Conditionals](../day-04-operators-and-conditionals/README.md)
