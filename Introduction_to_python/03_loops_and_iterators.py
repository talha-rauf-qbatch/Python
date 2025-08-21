# Loops and Iterators in Python

# ---------------------------
# 1. For Loop with range()
# ---------------------------
print("For Loop Example:")
for i in range(5):   # 0,1,2,3,4
    print("Iteration:", i)

# ---------------------------
# 2. While Loop
# ---------------------------
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1   # increment to avoid infinite loop

# ---------------------------
# 3. Simulating a Do-While Loop in Python
# ---------------------------

print("\nSimulated Do-While Example:")

number = 0
while True:
    print("Number is:", number)
    number += 1
    if number >= 5:   # condition check happens at the end
        break

# ---------------------------
# 4. Loop Control Statements
# ---------------------------
print("\nBreak and Continue:")
for i in range(10):
    if i == 5:
        break   # stop loop completely
    if i % 2 == 0:
        continue   # skip even numbers
    print("Odd number:", i)

# ---------------------------
# 5. Iterating over a List
# ---------------------------
fruits = ["apple", "banana", "cherry"]
print("\nLooping through a list:")
for fruit in fruits:
    print(fruit)

# ---------------------------
# 6. Iterating over a Dictionary
# ---------------------------
person = {"name": "Talha", "age": 22, "student": True}
print("\nLooping through a dictionary:")
for key, value in person.items():
    print(key, "->", value)

# ---------------------------
# 7. Nested Loops
# ---------------------------
print("\nNested Loops Example:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# ---------------------------
# 8. Iterators (under the hood of loops)
# ---------------------------
print("\nIterator Example:")
numbers = [10, 20, 30]
iterator = iter(numbers)   # create an iterator

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
# print(next(iterator)) # This will raise StopIteration

# ---------------------------
# 9. Using enumerate() in loops
# ---------------------------
print("\nUsing enumerate:")
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")

# ---------------------------
# 10. Using zip() in loops
# ---------------------------
print("\nUsing zip:")
names = ["Ali", "Sara", "John"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# ---------------------------
# 11. Conclusion
# ---------------------------
print("\nThis was a short intro to Loops and Iterators!")
