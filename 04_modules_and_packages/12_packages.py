# Packages in Python

# ---------------------------
# 1. Example Package Structure
# ---------------------------
# Suppose we create a package called "mypackage"
#
# mypackage/
#   __init__.py
#   greetings.py
#   math_ops.py
#
# greetings.py:
#   def say_hello(name):
#       return f"Hello, {name}"
#
# math_ops.py:
#   def add(a, b):
#       return a + b
#
# ---------------------------
# 2. Importing from a package
# ---------------------------
# You can use:
#   import mypackage.greetings
#   print(mypackage.greetings.say_hello("Talha"))
#
# Or import specific functions:
#   from mypackage.math_ops import add
#   print(add(10, 20))

print("Package example: Create a folder 'mypackage' with __init__.py and test imports!")

# ---------------------------
# 3. __init__.py Purpose
# ---------------------------
# - Tells Python that the folder is a package.
# - Can be used to control what is exposed when using `from mypackage import *`.
#
# Example __init__.py:
#   from .greetings import say_hello
#   from .math_ops import add

# ---------------------------
# 4. Installing External Packages
# ---------------------------
# Python has thousands of packages available via PyPI.
# Use pip to install:
#   pip install requests

# Example with requests package (make sure it's installed):
try:
    import requests
    response = requests.get("https://api.github.com")
    print("\nUsing external package 'requests':")
    print("GitHub API Status Code:", response.status_code)
except ImportError:
    print("\nPlease install 'requests' using: pip install requests")

# ---------------------------
# 5. Virtual Environments (Important for Packages)
# ---------------------------
# Best practice: use virtual environments to manage dependencies.
#   python -m venv venv
#   source venv/bin/activate   (Linux/Mac)
#   venv\Scripts\activate      (Windows)
#   pip install package_name

# ---------------------------
# 6. Conclusion
# ---------------------------
print("\nThis was an introduction to Packages in Python!")
