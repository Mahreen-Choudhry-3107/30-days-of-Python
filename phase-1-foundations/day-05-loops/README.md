# Day 05: Loops

> **Phase 1 – Foundations** | Estimated time: 2 hours

## 🎯 Learning objectives

- Repeat work with `for` and `while`.
- Use `range()`, `break`, `continue`, and loop `else`.
- Use `enumerate()` and `zip()`.
- Build patterns with nested loops.

## 📖 Concepts

### `for` loop

Iterates over any iterable (string, list, range, …).

```python
for ch in "abc":
    print(ch)

for fruit in ["apple", "mango"]:
    print(fruit)
```

### `range()`

```python
range(5)          # 0,1,2,3,4
range(2, 8)       # 2..7
range(10, 0, -2)  # 10,8,6,4,2

for i in range(1, 6):
    print(i, end=" ")      # 1 2 3 4 5
```

### `while` loop

Runs while a condition is true.

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
```

Use `while` when you do not know in advance how many iterations are needed (e.g. input validation).

```python
while True:
    pin = input("PIN: ")
    if pin == "1234":
        break
    print("Wrong PIN")
```

### `break`, `continue`, loop `else`

```python
for n in range(10):
    if n == 3:
        continue        # skip this iteration
    if n == 6:
        break           # exit the loop
    print(n)

for n in range(2, 10):
    if n == 11:
        break
else:
    print("No break happened")   # runs only if loop was not broken
```

### `enumerate()` and `zip()`

```python
names = ["Ali", "Sara", "Omar"]
for index, name in enumerate(names, start=1):
    print(index, name)

scores = [90, 85, 70]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### Nested loops – patterns

```python
for i in range(1, 5):
    print("*" * i)

# multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
```

### Accumulator pattern

```python
total = 0
for n in range(1, 101):
    total += n
print(total)    # 5050
```

### Useful built-ins

`sum()`, `min()`, `max()`, `len()`, `sorted()`, `reversed()`, `any()`, `all()`.

## ⚠️ Common mistakes

- Infinite `while` loops (forgetting to update the condition).
- Off-by-one with `range(n)` (it stops at `n - 1`).
- Modifying a list while looping over it.
- Using `range(len(x))` when `enumerate(x)` is cleaner.

## 🏋️ Exercises

1. Print the multiplication table of any number.
2. Sum all even numbers from 1 to 100.
3. Check whether a number is prime.
4. Print the first 10 Fibonacci numbers.
5. Print a pyramid pattern of height `n`.

## 🛠 Mini project: FizzBuzz + Password validator

1. FizzBuzz from 1 to 50 (multiples of 3 → "Fizz", 5 → "Buzz", both → "FizzBuzz").
2. Keep asking for a password until it has at least 8 characters, one digit, and one uppercase letter.

## 📝 Summary

- `for` iterates over iterables; `while` repeats on a condition.
- `break` exits, `continue` skips, loop `else` runs when no `break` occurred.
- `enumerate` and `zip` make loops cleaner.

⬅️ [Day 04](../day-04-operators-and-conditionals/README.md) | ➡️ [Day 06 – Lists & Tuples](../day-06-lists-and-tuples/README.md)
