# Sets in Python

# ---------------------------
# 1. Creating Sets
# ---------------------------
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate "apple" will be removed
print("Fruits Set:", fruits)

empty_set = set()   # correct way ( {} creates a dictionary )
print("Empty Set:", empty_set)

# ---------------------------
# 2. Adding Elements
# ---------------------------
fruits.add("orange")
print("\nAfter add():", fruits)

fruits.update(["mango", "grape"])   # add multiple
print("After update():", fruits)

# ---------------------------
# 3. Removing Elements
# ---------------------------
fruits.remove("banana")   # remove item (error if not found)
print("\nAfter remove():", fruits)

fruits.discard("kiwi")    # no error if not found
print("After discard():", fruits)

popped = fruits.pop()     # removes a random item
print("Popped item:", popped)
print("After pop():", fruits)

# ---------------------------
# 4. Set Operations
# ---------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nSet Operations:")
print("Union:", A | B)             # or A.union(B)
print("Intersection:", A & B)      # or A.intersection(B)
print("Difference A-B:", A - B)    # or A.difference(B)
print("Symmetric Difference:", A ^ B)  # or A.symmetric_difference(B)

# ---------------------------
# 5. Membership Test
# ---------------------------
print("\nMembership Test:")
print(2 in A)   # True
print(10 in A)  # False

# ---------------------------
# 6. Looping through a Set
# ---------------------------
print("\nLooping through Set:")
for fruit in fruits:
    print(fruit)

# ---------------------------
# 7. Frozen Sets (Immutable Set)
# ---------------------------
frozen = frozenset([1, 2, 3, 2])
print("\nFrozen Set:", frozen)
# frozen.add(4)  # ❌ Error: frozensets are immutable

# ---------------------------
# 8. Set Comprehension
# ---------------------------
squares = {x**2 for x in range(6)}
print("\nSet Comprehension:", squares)

# ---------------------------
# 9. Conclusion
# ---------------------------
print("\nThis was an introduction to Python Sets!")
