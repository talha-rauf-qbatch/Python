# Classes and Objects in Python

# ---------------------------
# 1. Defining a Simple Class
# ---------------------------
class Person:
    # Class attribute (shared by all objects)
    species = "Human"

    # Constructor (initializer)
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    # Method (behavior)
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# ---------------------------
# 2. Creating Objects
# ---------------------------
p1 = Person("Talha", 25)
p2 = Person("Ali", 30)

print(p1.greet())
print(p2.greet())

# Accessing class attribute
print("Species:", Person.species)

# ---------------------------
# 3. Modifying Attributes
# ---------------------------
p1.age = 26  # modify attribute
print(f"{p1.name} is now {p1.age} years old")

# ---------------------------
# 4. Adding Attributes Dynamically
# ---------------------------
p1.country = "Pakistan"  # dynamic attribute (only for this object)
print(f"{p1.name} is from {p1.country}")

# ---------------------------
# 5. Using __str__ for Readable Objects
# ---------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"Car({self.brand}, {self.model})"

car1 = Car("Toyota", "Corolla")
print(car1)  # Automatically calls __str__

# ---------------------------
# 6. Difference Between Class & Instance Attributes
# ---------------------------
class Dog:
    species = "Canine"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

dog1 = Dog("Buddy")
dog2 = Dog("Rocky")

print(dog1.name, "-", dog1.species)
print(dog2.name, "-", dog2.species)

# ---------------------------
# 7. Conclusion
# ---------------------------
print("\nThis was an introduction to Classes and Objects in Python!")
