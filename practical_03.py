"""
Practical 3: Conditional Statements (if, if-else, elif, nested if)
"""

# ---------- Question 1: Basic If ----------
print("----- Question 1 -----")
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")

# ---------- Question 2: If-Else ----------
print("\n----- Question 2 -----")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# ---------- Question 3: elif Grading ----------
print("\n----- Question 3 -----")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# ---------- Question 4: Nested If (Voting Eligibility) ----------
print("\n----- Question 4 -----")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18:
    if nationality.strip().lower() == "indian":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote because you are not an Indian citizen.")
else:
    print("You are not eligible to vote because you are under 18.")

# ---------- Question 5: Largest of Three Numbers ----------
print("\n----- Question 5 -----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

if a == b == c:
    print("All three numbers are equal.")

# ---------- Question 6: Leap Year Checker ----------
print("\n----- Question 6 -----")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")

# ---------- Question 7: Simple Calculator ----------
print("\n----- Question 7 -----")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid Operator.")

# ---------- Question 8: Discount Eligibility System ----------
print("\n----- Question 8 -----")
amount = float(input("Enter purchase amount: "))

if amount >= 2000:
    discount = amount * 0.20      # 20% discount
elif amount >= 1000:
    discount = amount * 0.10      # 10% discount
else:
    discount = 0                  # no discount

final_amount = amount - discount
print("Purchase Amount =", amount)
print("Discount =", discount)
print("Final Amount =", final_amount)

# ---------- Question 9: Triangle Type Identifier ----------
print("\n----- Question 9 -----")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# ---------- Question 10: Menu-Driven Program ----------
print("\n----- Question 10 -----")
print("----- MENU -----")
print("1. Check Even/Odd")
print("2. Find Largest of Three Numbers")
print("3. Grade System")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a >= b and a >= c:
        print("Largest =", a)
    elif b >= a and b >= c:
        print("Largest =", b)
    else:
        print("Largest =", c)
elif choice == 3:
    marks = int(input("Enter marks: "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")
else:
    print("Invalid Choice")
