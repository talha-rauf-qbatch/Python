# Basic Syntax Examples

# ---------------------------
# 1. Printing in Python
# ---------------------------
print("Hello, World!")  

# ---------------------------
# 2. Comments
# ---------------------------
# This is a single-line comment

"""
This is a multi-line comment.
It can be used to explain longer code sections.
"""

# ---------------------------
# 3. Variables and Data Types
# ---------------------------
name = "Talha"       # String
age = 22             # Integer
height = 5.9         # Float
is_student = True    # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student?", is_student)

# ---------------------------
# 4. Basic Arithmetic
# ---------------------------
x = 10
y = 3

print("Addition:", x + y)       # 13
print("Subtraction:", x - y)    # 7
print("Multiplication:", x * y) # 30
print("Division:", x / y)       # 3.333...
print("Floor Division:", x // y)# 3
print("Modulus:", x % y)        # 1
print("Power:", x ** y)         # 1000

# ---------------------------
# 5. Indentation & Blocks
# ---------------------------
if age > 18:
    print(name, "is an adult.")   # Indentation is required in Python
else:
    print(name, "is not an adult.")

# ---------------------------
# 6. Functions
# ---------------------------
def greet(person):
    return "Hello, " + person + "!"

print(greet(name))

# ---------------------------
# 7. Loops
# ---------------------------
for i in range(5):  # loop from 0 to 4
    print("Loop iteration:", i)

# ---------------------------
# 8. Conclusion
# ---------------------------
print("This was a short intro to Python basic syntax!")
