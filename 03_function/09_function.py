# Functions in Python

# ---------------------------
# 1. Basic Function
# ---------------------------
def greet():
    print("Hello, welcome to Python functions!")

greet()

# ---------------------------
# 2. Function with Parameters
# ---------------------------
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Talha")
greet_person("Sara")

# ---------------------------
# 3. Function with Return Value
# ---------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("\nAddition Result:", result)

# ---------------------------
# 4. Default Parameters
# ---------------------------
def power(base, exponent=2):   # default exponent is 2
    return base ** exponent

print("\nDefault Parameter Example:")
print("power(5) =", power(5))       # 5^2
print("power(2, 3) =", power(2, 3)) # 2^3

# ---------------------------
# 5. Keyword Arguments
# ---------------------------
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=22, name="Talha")

# ---------------------------
# 6. Arbitrary Arguments (*args)
# ---------------------------
def sum_all(*numbers):
    return sum(numbers)

print("\n*args Example:")
print("Sum:", sum_all(1, 2, 3, 4, 5))

# ---------------------------
# 7. Arbitrary Keyword Arguments (**kwargs)
# ---------------------------
def print_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n**kwargs Example:")
print_details(name="Ali", age=25, city="Lahore")

# ---------------------------
# 8. Returning Multiple Values
# ---------------------------
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calculate(10, 5)
print("\nMultiple Return Values:")
print("Sum:", sum_)
print("Difference:", diff)
print("Product:", prod)

# ---------------------------
# 9. Lambda (Anonymous Functions)
# ---------------------------
square = lambda x: x**2
print("\nLambda Function Example:")
print("Square of 6:", square(6))

# ---------------------------
# 10. Functions Inside Functions
# ---------------------------
def outer():
    def inner():
        return "Hello from inner function!"
    return inner()

print("\nNested Function Example:", outer())

# ---------------------------
# 11. Recursion (Function calling itself)
# ---------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("\nRecursion Example:")
print("Factorial of 5:", factorial(5))

# ---------------------------
# 12. Conclusion
# ---------------------------
print("\nThis was an introduction to Functions in Python!")
