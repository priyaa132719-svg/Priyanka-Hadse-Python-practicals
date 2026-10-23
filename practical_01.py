"""
Practical 1: Basics of Python - Variables, Constants, and Data Types
Subject: VBCS1101 Introduction to Programming
"""

# ---------- Question 1: Variable Creation and Naming Rules ----------
print("----- Question 1 -----")
name = "Asha"
age = 18
marks = 91.5
city = "Pune"
print(name, age, marks, city)

# Invalid names (uncomment to see SyntaxError):
# 1name = "Asha"    # cannot start with a digit
# class = "BSc"     # 'class' is a reserved keyword
# my-name = "Asha"  # '-' is the minus operator, not allowed in names

# Corrected names:
name1 = "Asha"
class_name = "BSc"
my_name = "Asha"
print(name1, class_name, my_name)

# ---------- Question 2: Dynamic Typing ----------
print("\n----- Question 2 -----")
value = 100
print(value)
print(type(value))

value = "Python"
print(value)
print(type(value))

value = 99.5
print(value)
print(type(value))
# In Python the type belongs to the value, so a variable can change type.
# In statically typed languages (C, Java) a variable's type is fixed.

# ---------- Question 3: Constants (by convention) ----------
print("\n----- Question 3 -----")
PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 100
print("PI =", PI)
print("GRAVITY =", GRAVITY)
print("MAX_USERS =", MAX_USERS)

# Changing the values (allowed in Python)
PI = 3.14
print("Updated PI =", PI)
# Python does not enforce constants. UPPERCASE names are only a convention.

# ---------- Question 4: Data Type Identification System ----------
print("\n----- Question 4 -----")
integer = int(input("Enter an integer: "))
floating = float(input("Enter a float: "))
string = input("Enter a string: ")
boolean = input("Enter True or False: ")
boolean = boolean.strip().lower() == "true"   # accepts true/True/TRUE

print("\nSummary")
print("---------------------------")
print("Value\t\tType")
print(integer, "\t\t", type(integer))
print(floating, "\t\t", type(floating))
print(string, "\t\t", type(string))
print(boolean, "\t\t", type(boolean))

# ---------- Question 5: Type Conversion (Casting) ----------
print("\n----- Question 5 -----")
age = input("Enter Age: ")
marks = input("Enter Marks: ")

print("Without Conversion:")
print(age + marks)        # strings get joined, e.g. "1897"
# print(age + 5)          # TypeError: can only concatenate str to str

age = int(age)
marks = float(marks)
print("Age after 5 years:", age + 5)
print("Marks + 2:", marks + 2)
# input() always returns a string, so use int()/float() for arithmetic.

# ---------- Question 6: Implicit vs Explicit Type Conversion ----------
print("\n----- Question 6 -----")
a = 10
b = 5.5
print(a + b)              # Implicit conversion: int -> float

# print(a + "5")          # TypeError
c = "5"
print(a + int(c))         # Explicit conversion

# ---------- Question 7: Memory Behavior of Variables ----------
print("\n----- Question 7 -----")
a = 100
b = 100
print(id(a))
print(id(b))              # same id: both refer to the same object

b = 200
print(id(a))
print(id(b))              # b now points to a new object
# Integers are immutable: changing a value creates a new object.

# ---------- Question 8: Swapping Variables ----------
print("\n----- Question 8 -----")
# Method 1: Third variable
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)

# Method 2: Tuple unpacking
a = 10
b = 20
a, b = b, a
print(a, b)
# Third variable uses extra memory; tuple unpacking is shorter and cleaner.

# ---------- Question 9: Data Type-Based Calculator ----------
print("\n----- Question 9 -----")
first = input("Enter first value: ")
second = input("Enter second value: ")

try:
    num1 = float(first)
    num2 = float(second)
    print("Addition =", num1 + num2)
except ValueError:
    if first.isalpha() and second.isalpha():
        print("Concatenation =", first + second)
    else:
        print("Invalid Input")

# ---------- Question 10: Boolean Logic and Data Types ----------
print("\n----- Question 10 -----")
age = int(input("Enter Age: "))
marks = int(input("Enter Marks: "))

is_adult = age > 18
is_passed = marks > 50

print("Adult:", is_adult)
print("Passed:", is_passed)

if is_adult and is_passed:
    print("Eligible")
else:
    print("Not Eligible")

# ---------- Question 11: Temperature Converter ----------
print("\n----- Question 11 -----")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
