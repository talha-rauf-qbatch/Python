# Conditions in Python

# ---------------------------
# 1. Basic if statement
# ---------------------------
age = 20

if age >= 18:
    print("You are an adult.")   # this runs if condition is True

# ---------------------------
# 2. if-else statement
# ---------------------------
is_student = False

if is_student:
    print("Discount applied!")
else:
    print("No discount available.")

# ---------------------------
# 3. if-elif-else statement
# ---------------------------
marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

# ---------------------------
# 4. Nested if statements
# ---------------------------
number = 15

if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is not positive")

# ---------------------------
# 5. Short-hand if (single line)
# ---------------------------
x = 10
if x > 5: print("x is greater than 5")

# ---------------------------
# 6. Short-hand if-else (ternary operator)
# ---------------------------
y = 20
result = "Even" if y % 2 == 0 else "Odd"
print("y is:", result)

# ---------------------------
# 7. Combining Conditions (and, or, not)
# ---------------------------
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("It's a good day to go outside!")

if temperature < 10 or is_raining:
    print("Better stay indoors.")

# ---------------------------
# 8. Membership & Identity Operators in Conditions
# ---------------------------
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list!")

a = [1, 2, 3]
b = a
if a is b:
    print("a and b refer to the same object in memory")

# ---------------------------
# 9. Conclusion
# ---------------------------
print("This was an introduction to Conditions in Python!")
