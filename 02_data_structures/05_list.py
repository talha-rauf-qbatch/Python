# Lists in Python

# ---------------------------
# 1. Creating Lists
# ---------------------------
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# ---------------------------
# 2. Accessing Elements
# ---------------------------
print("\nAccessing Elements:")
print("First fruit:", fruits[0])     # indexing
print("Last fruit:", fruits[-1])    # negative index
print("Slice:", fruits[0:2])        # slicing

# ---------------------------
# 3. Modifying Lists
# ---------------------------
print("\nModifying List:")
fruits[1] = "mango"    # change value
print("Updated Fruits:", fruits)

# ---------------------------
# 4. Adding Items
# ---------------------------
fruits.append("orange")    # add to end
fruits.insert(1, "grape")  # insert at index
print("\nAfter Adding:", fruits)

# ---------------------------
# 5. Removing Items
# ---------------------------
fruits.remove("apple")     # remove by value
removed_item = fruits.pop()   # removes last item
print("\nAfter Removing:", fruits)
print("Popped Item:", removed_item)

del fruits[0]   # delete by index
print("After del:", fruits)

# ---------------------------
# 6. Iterating over Lists
# ---------------------------
print("\nLooping through list:")
for fruit in fruits:
    print(fruit)

# ---------------------------
# 7. List Functions
# ---------------------------
nums = [10, 5, 8, 20]
print("\nList Functions:")
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sorted:", sorted(nums))
print("Sum:", sum(nums))

# ---------------------------
# 8. List Comprehension
# ---------------------------
print("\nList Comprehension:")
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# ---------------------------
# 9. Nested Lists (Matrix)
# ---------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix Example:")
print("Row 1:", matrix[0])
print("Element at (2,3):", matrix[1][2])

# ---------------------------
# 10. Copying Lists
# ---------------------------
original = [1, 2, 3]
copy_list = original[:]  # shallow copy
copy_list.append(4)
print("\nOriginal:", original)
print("Copy:", copy_list)

# ---------------------------
# 11. Conclusion
# ---------------------------
print("\nThis was an introduction to Python Lists!")
