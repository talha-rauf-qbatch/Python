# File Handling in Python

# ---------------------------
# 1. Opening a File
# ---------------------------
# Modes:
#   "r"  - read (default)
#   "w"  - write (overwrite if exists, create if not)
#   "a"  - append (add new data without overwriting)
#   "x"  - create (fails if file exists)
#   "b"  - binary mode
#   "t"  - text mode (default)

# Let's create and write into a file
f = open("sample.txt", "w")   # open file in write mode
f.write("Hello, Python!\n")
f.write("This is my first file handling example.\n")
f.close()

# ---------------------------
# 2. Reading from a File
# ---------------------------
f = open("sample.txt", "r")   # open file in read mode
print("Reading full file:\n", f.read())
f.close()

# Read line by line
f = open("sample.txt", "r")
print("\nReading line by line:")
for line in f:
    print(line.strip())  # strip() removes extra spaces/newlines
f.close()

# ---------------------------
# 3. Append to a File
# ---------------------------
f = open("sample.txt", "a")
f.write("Appending a new line.\n")
f.close()

# ---------------------------
# 4. Using with (Context Manager)
# ---------------------------
# 'with' automatically closes the file after use
with open("sample.txt", "r") as f:
    print("\nUsing with statement:\n", f.read())

# ---------------------------
# 5. File Methods
# ---------------------------
with open("sample.txt", "r") as f:
    print("\nFile Name:", f.name)
    print("Mode:", f.mode)
    print("Is Closed?", f.closed)

print("After 'with', file closed automatically:", f.closed)

# ---------------------------
# 6. Working with Binary Files
# ---------------------------
# Writing binary data
with open("binary_file.bin", "wb") as f:
    f.write(b"This is binary data.")

# Reading binary data
with open("binary_file.bin", "rb") as f:
    data = f.read()
    print("\nBinary file content:", data)

# ---------------------------
# 7. Exception Handling in File Operations
# ---------------------------
try:
    with open("non_existent.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("\nError:", e)

# ---------------------------
# 8. Conclusion
# ---------------------------
print("\nThis was an introduction to File Handling in Python!")
