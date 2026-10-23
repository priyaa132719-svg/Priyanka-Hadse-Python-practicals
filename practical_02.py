"""
Practical 2: Input/Output Operations and Arithmetic Expressions
"""
import math

# ---------- Question 1: Simple print vs f-string ----------
print("----- Question 1 -----")
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)
print(f"Name: {name}, Age: {age}")

# ---------- Question 2: Numeric Input Handling ----------
print("\n----- Question 2 -----")
a = input("Enter first number: ")
b = input("Enter second number: ")
print("Addition without conversion:", a + b)   # "10" + "20" -> "1020"

a = int(a)
b = int(b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Division: not possible (division by zero)")

# ---------- Question 3: Expression Evaluation ----------
print("\n----- Question 3 -----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum_value = a + b + c
average = sum_value / 3
expression = (a + b) * c / 2

print("Sum =", sum_value)
print("Average =", average)
print("Expression =", expression)

# ---------- Question 4: Operator Precedence ----------
print("\n----- Question 4 -----")
print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)
print("100 / 5 + 3 * 2 =", 100 / 5 + 3 * 2)
# Predicted: 20, 30, 26.0
# Multiplication/division are evaluated before addition; parentheses first.

# ---------- Question 5: Salary Breakdown ----------
print("\n----- Question 5 -----")
basic = float(input("Enter Basic Salary: "))
hra = basic * 0.20
da = basic * 0.10
net_salary = basic + hra + da

print("\nSalary Breakdown")
print("Basic Salary =", basic)
print("HRA (20%) =", hra)
print("DA (10%) =", da)
print("Net Salary =", net_salary)

# ---------- Question 6: Area and Perimeter Calculator ----------
print("\n----- Question 6 -----")
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print("\nRectangle")
print(f"Area = {rect_area}")
print(f"Perimeter = {rect_perimeter}")

radius = float(input("\nEnter circle radius: "))
circle_area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("\nCircle")
print(f"Area = {circle_area:.2f}")
print(f"Circumference = {circumference:.2f}")

# ---------- Question 7: Unit Conversion Tool ----------
print("\n----- Question 7 -----")
km = float(input("Enter distance in kilometers: "))
meters = km * 1000

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

rupees = float(input("Enter amount in Rupees: "))
rate = 85                       # fixed exchange rate (Rs per dollar)
dollars = rupees / rate

print(f"{km} km = {meters} meters")
print(f"{celsius}°C = {fahrenheit:.2f}°F")
print(f"Rs {rupees} = ${dollars:.2f}")

# ---------- Question 8: Multi-Input Single-Line Processing ----------
print("\n----- Question 8 -----")
a, b, c = map(int, input("Enter three numbers separated by space: ").split())
sum_value = a + b + c
product = a * b * c
print(f"Numbers: {a}, {b}, {c}")
print(f"Sum = {sum_value}")
print(f"Product = {product}")

# ---------- Question 9: Expression-Based Grading System ----------
print("\n----- Question 9 -----")
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)

# ---------- Question 10: Error Analysis in Expressions ----------
print("\n----- Question 10 -----")
# Errors (handled with try-except so the program keeps running)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")

num = 10
denominator = 2
result = num / denominator
print("Correct Division =", result)

try:
    result = "10" + 5
except TypeError:
    print("Cannot add a string and an integer directly.")

result = int("10") + 5
print("Correct Addition =", result)
