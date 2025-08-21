# Inheritance in Python

# ---------------------------
# 1. Simple (Single) Inheritance
# ---------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # overriding method
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy")
print(dog1.speak())  # calls overridden method

# ---------------------------
# 2. Using super() to Call Parent Class
# ---------------------------
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # call parent constructor
        self.color = color

    def speak(self):
        return f"{self.name} (a {self.color} cat) says Meow!"

cat1 = Cat("Kitty", "white")
print(cat1.speak())

# ---------------------------
# 3. Multi-Level Inheritance
# ---------------------------
class BabyDog(Dog):  # BabyDog inherits from Dog (which inherits from Animal)
    def play(self):
        return f"{self.name} loves to play!"

puppy = BabyDog("Tommy")
print(puppy.speak())  # inherited from Dog
print(puppy.play())   # defined in BabyDog

# ---------------------------
# 4. Multiple Inheritance
# ---------------------------
class Walker:
    def walk(self):
        return "I can walk!"

class Flyer:
    def fly(self):
        return "I can fly!"

class Bird(Walker, Flyer):  # inherits from multiple parents
    pass

parrot = Bird()
print(parrot.walk())
print(parrot.fly())

# ---------------------------
# 5. Method Resolution Order (MRO)
# ---------------------------
print(Bird.mro())  # shows the order Python searches for methods

# ---------------------------
# 6. isinstance() and issubclass()
# ---------------------------
print(isinstance(parrot, Bird))   # True
print(isinstance(parrot, Walker)) # True
print(issubclass(Bird, Flyer))    # True
print(issubclass(Dog, Animal))    # True

# ---------------------------
# 7. Conclusion
# ---------------------------
print("\nThis was an introduction to Inheritance in Python!")
