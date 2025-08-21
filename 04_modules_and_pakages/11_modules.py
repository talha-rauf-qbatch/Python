# Modules in Python

# ---------------------------
# 1. Importing the whole module
# ---------------------------
import math   # built-in math module

print("Using math module:")
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))

# ---------------------------
# 2. Importing specific functions/variables
# ---------------------------
from math import pi, pow

print("\nImporting specific items:")
print("Value of pi:", pi)
print("2^3 using pow:", pow(2, 3))

# ---------------------------
# 3. Importing with alias
# ---------------------------
import math as m

print("\nUsing alias:")
print("cos(0):", m.cos(0))

# ---------------------------
# 4. Custom Modules
# ---------------------------
# You can create your own module (a .py file) and import it.
# Example:
#   Create a file called mymodule.py with a function:
#       def greet(name): return f"Hello, {name}"
#
# Then you can do:
#   import mymodule
#   print(mymodule.greet("Talha"))

print("\n(Custom module example would go here if you create mymodule.py)")

# ---------------------------
# 5. Using 'as' for custom modules
# ---------------------------
#   import mymodule as mm
#   print(mm.greet("Ali"))

# ---------------------------
# 6. Using 'from ... import *'
# ---------------------------
# (Not recommended in real projects, but valid)
#   from mymodule import *
#   print(greet("Sara"))

# ---------------------------
# 7. Exploring Module Contents
# ---------------------------
print("\nAvailable functions in math module:")
print(dir(math))   # shows all attributes & functions of math module

# ---------------------------
# 8. Standard Library Example (random module)
# ---------------------------
import random

print("\nRandom module example:")
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(["apple", "banana", "cherry"]))

# ---------------------------
# 9. Importing Packages
# ---------------------------
# A package is a collection of modules inside a folder with __init__.py
# Example: 'numpy' is a popular package for numerical computing.
#   import numpy as np
#   arr = np.array([1, 2, 3])
#   print(arr)

print("\n(Package example: install numpy and import as np to test)")

# ---------------------------
# 10. Conclusion
# ---------------------------
print("\nThis was an introduction to Modules in Python!")
