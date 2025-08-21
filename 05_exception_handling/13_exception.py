# Exception Handling in Python

# ---------------------------
# 1. Basic try-except
# ---------------------------
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# ---------------------------
# 2. Multiple except blocks
# ---------------------------
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid conversion to integer!")
except TypeError:
    print("Error: Wrong type used!")

# ---------------------------
# 3. Catching multiple exceptions in one block
# ---------------------------
try:
    lst = [1, 2, 3]
    print(lst[5])
except (IndexError, KeyError) as e:
    print("Caught an error:", e)

# ---------------------------
# 4. Using else with try-except
# ---------------------------
try:
    result = 5 / 1
except ZeroDivisionError:
    print("Division error!")
else:
    print("Division successful, result =", result)

# ---------------------------
# 5. Using finally (always executes)
# ---------------------------
try:
    f = open("test.txt", "w")
    f.write("Hello Exception Handling")
except IOError:
    print("File writing error!")
finally:
    f.close()
    print("File closed (finally block executed).")

# ---------------------------
# 6. Raising Exceptions Manually
# ---------------------------
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        print("Valid age:", age)

try:
    check_age(-5)
except ValueError as e:
    print("Caught Exception:", e)

# ---------------------------
# 7. Custom Exceptions
# ---------------------------
class MyCustomError(Exception):
    """Custom exception class"""
    pass

def test_value(x):
    if x > 100:
        raise MyCustomError("Value cannot be greater than 100!")

try:
    test_value(150)
except MyCustomError as e:
    print("Custom Exception:", e)

# ---------------------------
# 8. Conclusion
# ---------------------------
print("\nThis was an introduction to Exception Handling in Python!")
