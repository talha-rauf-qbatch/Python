# Abstraction in Python

from abc import ABC, abstractmethod

# ---------------------------
# 1. Abstract Class and Abstract Method
# ---------------------------
class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Cannot create object of abstract class:
# shape = Shape()  # ❌ Error

# ---------------------------
# 2. Concrete Classes Implement Abstract Methods
# ---------------------------
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

shapes = [Rectangle(5, 3), Circle(7)]
for s in shapes:
    print(f"Area: {s.area()}, Perimeter: {s.perimeter()}")

# ---------------------------
# 3. Partial Abstraction
# ---------------------------
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

    def info(self):  # normal method in abstract class
        return f"This is a vehicle of brand {self.brand}"

class Car(Vehicle):
    def start(self):
        return f"{self.brand} Car started!"

car1 = Car("Toyota")
print(car1.info())
print(car1.start())

# ---------------------------
# 4. Interface-like Abstraction
# ---------------------------
# In Python, abstract classes can act like interfaces (only abstract methods).
class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyer):
    def fly(self):
        return "Bird is flying!"

class Airplane(Flyer):
    def fly(self):
        return "Airplane is flying in the sky!"

flyers = [Bird(), Airplane()]
for f in flyers:
    print(f.fly())

# ---------------------------
# 5. Conclusion
# ---------------------------
print("\nThis was an introduction to Abstraction in Python!")
