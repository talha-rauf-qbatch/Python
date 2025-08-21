# Dictionaries in Python

# ---------------------------
# 1. Creating Dictionaries
# ---------------------------
person = {
    "name": "Talha",
    "age": 22,
    "is_student": True
}

print("Dictionary:", person)

# ---------------------------
# 2. Accessing Values
# ---------------------------
print("\nAccessing Values:")
print("Name:", person["name"])       # using key
print("Age:", person.get("age"))     # using get() method
print("Country (with default):", person.get("country", "Not Found"))

# ---------------------------
# 3. Modifying Values
# ---------------------------
person["age"] = 23        # update value
person["city"] = "Lahore" # add new key-value
print("\nUpdated Dictionary:", person)

# ---------------------------
# 4. Removing Items
# ---------------------------
person.pop("is_student")  # remove key
print("\nAfter pop():", person)

del person["city"]        # delete key
print("After del:", person)

# person.clear()          # remove all items

# ---------------------------
# 5. Looping through Dictionary
# ---------------------------
print("\nLooping through Dictionary:")
for key in person:
    print("Key:", key, "Value:", person[key])

print("\nUsing items():")
for key, value in person.items():
    print(key, "->", value)

# ---------------------------
# 6. Dictionary Methods
# ---------------------------
student = {"name": "Ali", "marks": 90}
print("\nDictionary Methods:")
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# update() method
student.update({"marks": 95, "grade": "A"})
print("Updated Student:", student)

# ---------------------------
# 7. Nested Dictionaries
# ---------------------------
classroom = {
    "student1": {"name": "Sara", "age": 20},
    "student2": {"name": "John", "age": 21}
}
print("\nNested Dictionary:", classroom)
print("Student1 Name:", classroom["student1"]["name"])

# ---------------------------
# 8. Dictionary Comprehension
# ---------------------------
squares = {x: x**2 for x in range(5)}
print("\nDictionary Comprehension:", squares)

# ---------------------------
# 9. Using dict() constructor
# ---------------------------
new_dict = dict(name="Zara", age=25)
print("\nUsing dict() constructor:", new_dict)

# ---------------------------
# 10. Conclusion
# ---------------------------
print("\nThis was an introduction to Python Dictionaries!")
