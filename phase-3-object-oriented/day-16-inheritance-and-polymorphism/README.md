# Day 16: Inheritance & Polymorphism

> **Phase 3 – Object-Oriented Python** | Estimated time: 2.5 hours

## 🎯 Learning objectives

- Reuse code through inheritance.
- Override methods and call `super()`.
- Apply polymorphism and duck typing.
- Define abstract base classes.
- Choose composition when appropriate.

## 📖 Concepts

### Inheritance

A child class inherits attributes and methods from a parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):               # overriding
        return f"{self.name} says woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"
```

### `super()`

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)    # reuse parent's initializer
        self.team = team
```

### Polymorphism

Different classes respond to the same method call in their own way.

```python
animals = [Dog("Rex"), Cat("Tom"), Animal("Generic")]
for a in animals:
    print(a.speak())
```

### Duck typing

"If it walks like a duck and quacks like a duck, it is a duck." Python cares about the **behavior** an object offers, not its declared type.

```python
class Robot:
    def speak(self):
        return "beep"

for thing in [Dog("Rex"), Robot()]:
    print(thing.speak())      # works without a shared parent
```

### Checking relationships

```python
isinstance(Dog("a"), Animal)      # True
issubclass(Dog, Animal)           # True
```

### Multiple inheritance and MRO

```python
class A:
    def hello(self): return "A"
class B(A):
    def hello(self): return "B"
class C(A):
    def hello(self): return "C"
class D(B, C):
    pass

D().hello()            # "B"
D.__mro__              # method resolution order: D, B, C, A, object
```

Python uses the **C3 linearization** to decide the lookup order. Use multiple inheritance mostly for **mixins** (small classes that add one behavior).

### Abstract base classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2

# Shape()  -> TypeError: can't instantiate abstract class
print(Circle(2).area())
```

### Composition ("has-a") vs inheritance ("is-a")

```python
class Engine:
    def start(self): return "Engine on"

class Car:
    def __init__(self):
        self.engine = Engine()        # a Car HAS an Engine
    def start(self):
        return self.engine.start()
```

Prefer composition when the relationship is not truly "is-a". A deep inheritance hierarchy becomes brittle.

### Mixins

```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JsonMixin):
    def __init__(self, name):
        self.name = name

print(User("Ali").to_json())
```

## ⚠️ Common mistakes

- Forgetting `super().__init__()` in a child constructor.
- Deep inheritance trees; prefer composition.
- Using inheritance only to share a few lines of code.
- Overriding a method with an incompatible signature.

## 🏋️ Exercises

1. Create `Vehicle` → `Car` and `Bike` with a `wheels` attribute and a `describe()` method.
2. Make an abstract `Payment` class with `pay(amount)`; implement `CardPayment` and `WalletPayment`.
3. Show polymorphism by looping through a list of different shapes and printing their areas.
4. Use a mixin to add logging to two unrelated classes.
5. Print the MRO of a diamond-shaped hierarchy and explain it.

## 🛠 Mini project: Employee payroll

Create `Employee` (base), `FullTime`, `PartTime`, and `Intern` classes with different salary calculations. Process a mixed list and print each pay slip.

## 📝 Summary

- Inheritance reuses code; `super()` calls the parent.
- Polymorphism and duck typing allow flexible code.
- Abstract base classes enforce interfaces.
- Prefer composition when "is-a" does not fit.

⬅️ [Day 15](../day-15-classes-and-objects/README.md) | ➡️ [Day 17 – Encapsulation & Dunder Methods](../day-17-encapsulation-and-dunder-methods/README.md)
