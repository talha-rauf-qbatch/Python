# Encapsulation in Python

# ---------------------------
# 1. Public Members
# ---------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # public attribute
        self.model = model      # public attribute

    def display(self):          # public method
        return f"Car: {self.brand}, Model: {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.display())
print(car1.brand)   # accessible directly

# ---------------------------
# 2. Protected Members (convention: _single_underscore)
# ---------------------------
class Bike:
    def __init__(self, brand):
        self._brand = brand  # protected attribute (should not be accessed directly)

    def _show(self):         # protected method
        return f"This is a {self._brand} bike."

bike1 = Bike("Honda")
print(bike1._brand)  # possible but discouraged
print(bike1._show()) # possible but discouraged

# ---------------------------
# 3. Private Members (name mangling with __double_underscore)
# ---------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Talha", 5000)
print(acc.owner)
# print(acc.__balance)   # ❌ AttributeError (private)
print(acc.get_balance()) # ✅ safe access
acc.deposit(2000)
print("After deposit:", acc.get_balance())

# Accessing private using name mangling (not recommended)
print("Hacky access:", acc._BankAccount__balance)

# ---------------------------
# 4. Encapsulation with Setter/Getter
# ---------------------------
class Student:
    def __init__(self, name):
        self.__name = name

    def set_name(self, new_name):  # setter
        self.__name = new_name

    def get_name(self):            # getter
        return self.__name

stu = Student("Ali")
print(stu.get_name())
stu.set_name("Ahmed")
print(stu.get_name())

# ---------------------------
# 5. Using @property Decorator (Pythonic way)
# ---------------------------
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):   # getter
        return self.__salary

    @salary.setter
    def salary(self, new_salary):  # setter
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

emp = Employee(40000)
print(emp.salary)   # calls @property
emp.salary = 50000 # calls @salary.setter
print(emp.salary)

# ---------------------------
# 6. Conclusion
# ---------------------------
print("\nThis was an introduction to Encapsulation in Python!")
