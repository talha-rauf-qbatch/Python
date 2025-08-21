# Tuples in Python

# ---------------------------
# 1. Creating Tuples
# ---------------------------
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

print("Fruits Tuple:", fruits)
print("Numbers Tuple:", numbers)
print("Mixed Tuple:", mixed)

# ---------------------------
# 2. Single-element Tuple
# ---------------------------
single = ("hello",)   # must include a comma
not_tuple = ("hello") # this is just a string

print("\nSingle-element Tuple:", single, type(single))
print("Not a Tuple:", not_tuple, type(not_tuple))

# ---------------------------
# 3. Accessing Elements
# ---------------------------
print("\nAccessing Elements:")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice:", fruits[0:2])

# ---------------------------
# 4. Immutability
# ---------------------------
# fruits[1] = "mango"   # ❌ Error: Tuples cannot be changed
print("\nTuples are immutable, so you cannot modify them directly.")

# ---------------------------
# 5. Looping through Tuples
# ---------------------------
print("\nLooping through Tuple:")
for fruit in fruits:
    print(fruit)

# ---------------------------
# 6. Tuple Functions
# ---------------------------
nums = (10, 5, 8, 20, 5)
print("\nTuple Functions:")
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Count of 5:", nums.count(5))
print("Index of 8:", nums.index(8))

# ---------------------------
# 7. Nesting Tuples
# ---------------------------
nested = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple:", nested)
print("Element at (2,2):", nested[1][1])

# ---------------------------
# 8. Tuple Packing and Unpacking
# ---------------------------
person = ("Talha", 22, "Student")
name, age, status = person   # unpacking
print("\nUnpacking Tuple:")
print("Name:", name)
print("Age:", age)
print("Status:", status)

# ---------------------------
# 9. Converting Between List and Tuple
# ---------------------------
list_version = list(fruits)   # convert tuple to list
list_version.append("mango")
new_tuple = tuple(list_version)   # convert back to tuple

print("\nConversion Example:")
print("List Version:", list_version)
print("New Tuple:", new_tuple)

# ---------------------------
# 10. Conclusion
# ---------------------------
print("\nThis was an introduction to Python Tuples!")
