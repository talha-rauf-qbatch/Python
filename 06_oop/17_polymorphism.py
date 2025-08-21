# Polymorphism in Python

# ---------------------------
# 1. Polymorphism with Methods
# ---------------------------
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # same method name, different behavior

# ---------------------------
# 2. Polymorphism with Functions
# ---------------------------
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Woof!
animal_sound(Cat())  # Meow!

# ---------------------------
# 3. Polymorphism with Inheritance
# ---------------------------
class Bird:
    def intro(self):
        return "There are many types of birds."
    def flight(self):
        return "Some birds can fly."

class Sparrow(Bird):
    def flight(self):
        return "Sparrows can fly."

class Penguin(Bird):
    def flight(self):
        return "Penguins cannot fly."

for bird in [Sparrow(), Penguin()]:
    print(bird.intro())
    print(bird.flight())

# ---------------------------
# 4. Built-in Polymorphism (len, +, etc.)
# ---------------------------
print(len("Hello"))   # works on string
print(len([1, 2, 3])) # works on list

print("Hello " + "World")  # + works as string concatenation
print(10 + 20)             # + works as arithmetic addition

# ---------------------------
# 5. Duck Typing in Python
# ---------------------------
# "If it looks like a duck, swims like a duck, and quacks like a duck, then it is a duck."

class Duck:
    def sound(self):
        return "Quack!"

class Person:
    def sound(self):
        return "Hello, I'm mimicking a duck: Quack!"

def make_it_sound(obj):
    print(obj.sound())

make_it_sound(Duck())
make_it_sound(Person())

# ---------------------------
# 6. Operator Overloading
# ---------------------------
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

book1 = Book(100)
book2 = Book(200)
print("Total pages:", book1 + book2)  # polymorphism with +

# ---------------------------
# 7. Conclusion
# ---------------------------
print("\nThis was an introduction to Polymorphism in Python!")
