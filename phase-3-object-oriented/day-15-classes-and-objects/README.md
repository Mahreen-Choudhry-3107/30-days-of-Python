# Day 15: Classes & Objects

> **Phase 3 – Object-Oriented Python** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Understand classes, objects, attributes, and methods.
- Write constructors with `__init__`.
- Differentiate instance and class attributes.
- Know when OOP is a good fit.

## 📖 Concepts

### Why OOP?

Object-Oriented Programming bundles **data** (attributes) and **behavior** (methods) into objects. It helps model real-world entities and organize larger programs.

### Class and object

A **class** is a blueprint; an **object** (instance) is a concrete thing built from it.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name        # instance attributes
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

rex = Dog("Rex", 3)
print(rex.name)       # Rex
print(rex.bark())     # Rex says woof!
```

### `self`

`self` is the instance on which the method is called. Python passes it automatically: `rex.bark()` is equivalent to `Dog.bark(rex)`.

### `__init__`

The initializer runs when an object is created. It sets up the instance's starting state.

### Instance vs class attributes

```python
class Student:
    school = "City School"          # class attribute (shared)
    count = 0

    def __init__(self, name):
        self.name = name            # instance attribute (per object)
        Student.count += 1

a = Student("Ali")
b = Student("Sara")
print(Student.count)    # 2
print(a.school)         # City School
```

Be careful: assigning `a.school = "X"` creates a new **instance** attribute that hides the class attribute for `a`.

### Methods that change state

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

acc = BankAccount("Ali", 1000)
acc.deposit(500)
print(acc.balance)     # 1500
```

### Objects are references

```python
a = BankAccount("Ali")
b = a
b.deposit(100)
print(a.balance)       # 100 (same object)
```

### Useful introspection

```python
type(acc)
isinstance(acc, BankAccount)
acc.__dict__          # instance attributes as a dict
hasattr(acc, "balance")
getattr(acc, "balance")
setattr(acc, "balance", 10)
dir(acc)
```

### `__str__` and `__repr__` (preview)

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print(Point(1, 2))     # Point(1, 2)
```

### When to use a class

Use classes when you have **state + behavior** that belong together, or many instances of the same concept. Simple functions are often enough for stateless work.

## ⚠️ Common mistakes

- Forgetting `self` in method definitions or when accessing attributes.
- Mutable class attributes shared accidentally (`items = []` at class level).
- Confusing class and instance attributes.
- Overusing classes for simple tasks.

## 🏋️ Exercises

1. Create a `Rectangle` class with `area()` and `perimeter()`.
2. Create a `Student` class that stores marks and returns the average and grade.
3. Create a `Counter` class with `increment`, `decrement`, and `reset`.
4. Extend `BankAccount` with a transaction history list.
5. Create a `Book` class and a list of books; find the most expensive.

## 🛠 Mini project: Inventory item system

Create an `Item` class (name, price, quantity) and an `Inventory` class that adds, removes, searches, and reports total stock value.

## 📝 Summary

- Classes are blueprints; objects are instances.
- `__init__` initializes state; `self` refers to the instance.
- Class attributes are shared; instance attributes are per object.

⬅️ [Day 14](../../phase-2-intermediate/day-14-review-and-expense-tracker/README.md) | ➡️ [Day 16 – Inheritance & Polymorphism](../day-16-inheritance-and-polymorphism/README.md)
