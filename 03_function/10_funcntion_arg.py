# Function Arguments in Python

# ---------------------------
# 1. Positional Arguments
# ---------------------------
def greet(name, age):
    print(f"My name is {name} and I am {age} years old.")

print("Positional Arguments Example:")
greet("Talha", 22)

# ---------------------------
# 2. Keyword Arguments
# ---------------------------
print("\nKeyword Arguments Example:")
greet(age=25, name="Ali")

# ---------------------------
# 3. Default Arguments
# ---------------------------
def power(base, exponent=2):  # exponent defaults to 2
    return base ** exponent

print("\nDefault Arguments Example:")
print("power(3) =", power(3))       # uses default exponent=2
print("power(3, 4) =", power(3, 4)) # override default

# ---------------------------
# 4. Variable-length Arguments (*args)
# ---------------------------
def add_all(*numbers):
    print("Numbers received:", numbers)
    return sum(numbers)

print("\n*args Example:")
print("Sum:", add_all(1, 2, 3, 4, 5))

# ---------------------------
# 5. Variable-length Keyword Arguments (**kwargs)
# ---------------------------
def show_details(**info):
    print("Details received as dictionary:")
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n**kwargs Example:")
show_details(name="Sara", age=21, city="Karachi")

# ---------------------------
# 6. Mixing *args and **kwargs
# ---------------------------
def demo(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

print("\nMixing *args and **kwargs Example:")
demo(10, 20, 30, 40, city="Lahore", country="Pakistan")

# ---------------------------
# 7. Passing Lists/Tuples with * (Unpacking)
# ---------------------------
def multiply(x, y, z):
    return x * y * z

nums = [2, 3, 4]
print("\nUnpacking List Example:")
print("multiply(*nums) =", multiply(*nums))

# ---------------------------
# 8. Passing Dict with ** (Unpacking)
# ---------------------------
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, from {city}.")

person = {"name": "John", "age": 30, "city": "London"}
print("\nUnpacking Dict Example:")
introduce(**person)

# ---------------------------
# 9. Keyword-only Arguments
# ---------------------------
def info(name, *, age, city):
    print(f"{name} is {age} years old from {city}.")

print("\nKeyword-only Arguments Example:")
info("Talha", age=22, city="Lahore")

# ---------------------------
# 10. Conclusion
# ---------------------------
print("\nThis was an introduction to Function Arguments in Python!")
