# Python Data Types

# ---------------------------
# 1. Numbers (int, float, complex)
# ---------------------------
integer_num = 10        # int
float_num = 3.14        # float
complex_num = 2 + 3j    # complex

print("Integer:", integer_num, type(integer_num))
print("Float:", float_num, type(float_num))
print("Complex:", complex_num, type(complex_num))

# ---------------------------
# 2. Strings (str)
# ---------------------------
message = "Hello, Python!"
print("String:", message, type(message))
print("First character:", message[0])   # indexing
print("Substring:", message[0:5])       # slicing
print("Uppercase:", message.upper())

# ---------------------------
# 3. Booleans (bool)
# ---------------------------
is_active = True
is_admin = False
print("Boolean values:", is_active, is_admin, type(is_active))

# ---------------------------
# 4. Lists (ordered, mutable)
# ---------------------------
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, type(fruits))
fruits.append("orange")    # add item
print("Updated List:", fruits)
print("First fruit:", fruits[0])   # indexing

# ---------------------------
# 5. Tuples (ordered, immutable)
# ---------------------------
coordinates = (10.5, 20.3)
print("Tuple:", coordinates, type(coordinates))
print("First coordinate:", coordinates[0])

# ---------------------------
# 6. Sets (unordered, unique values)
# ---------------------------
unique_numbers = {1, 2, 3, 3, 4}
print("Set (duplicates removed):", unique_numbers, type(unique_numbers))
unique_numbers.add(5)
print("Updated Set:", unique_numbers)

# ---------------------------
# 7. Dictionaries (key-value pairs)
# ---------------------------
person = {
    "name": "Talha",
    "age": 22,
    "is_student": True
}
print("Dictionary:", person, type(person))
print("Access by key:", person["name"])
person["age"] = 23  # update value
print("Updated Dictionary:", person)

# ---------------------------
# 8. NoneType (represents nothing)
# ---------------------------
nothing = None
print("None value:", nothing, type(nothing))