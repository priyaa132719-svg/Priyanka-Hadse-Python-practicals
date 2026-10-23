"""
Practical 4: Looping Statements (for, while, nested loops)
"""

# ---------- Question 1: for loop and range ----------
print("----- Question 1 -----")
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\nEven numbers from 1 to 10:")
for i in range(2, 11, 2):
    print(i)
# range(start, stop, step): start is included, stop is excluded,
# step is the increment. range(1, 11) -> 1..10, range(2, 11, 2) -> 2,4,6,8,10

# ---------- Question 2: while loop ----------
print("\n----- Question 2 -----")
i = 1
while i <= 10:
    print(i)
    i += 1
# for: used when the number of iterations is known.
# while: used when iterations depend on a condition.

# ---------- Question 3: Sum and Average ----------
print("\n----- Question 3 -----")
n = int(input("Enter how many numbers: "))
total = 0                      # not named 'sum' so the built-in sum() is not hidden
for i in range(n):
    num = int(input("Enter a number: "))
    total += num

if n > 0:
    average = total / n
    print("Sum =", total)
    print("Average =", average)
else:
    print("No numbers entered.")

# ---------- Question 4: Factorial ----------
print("\n----- Question 4 -----")
num = int(input("Enter a number: "))

# Using for loop
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial (for) =", fact)

# Using while loop
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("Factorial (while) =", fact)

# ---------- Question 5: Multiplication Table ----------
print("\n----- Question 5 -----")
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ---------- Question 6: Reverse and Palindrome ----------
print("\n----- Question 6 -----")
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# ---------- Question 7: Count Digits, Even and Odd ----------
print("\n----- Question 7 -----")
num = int(input("Enter a number: "))
digits = 0
even = 0
odd = 0
while num > 0:
    digit = num % 10
    digits += 1
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print("Total Digits =", digits)
print("Even Digits =", even)
print("Odd Digits =", odd)

# ---------- Question 8: Prime Number Checker ----------
print("\n----- Question 8 -----")
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
# Optimization: check divisors only up to the square root of the number.

# ---------- Question 9: Fibonacci Series ----------
print("\n----- Question 9 -----")
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()

# ---------- Question 10: Nested Loops (Patterns) ----------
print("\n----- Question 10 -----")
rows = 4

print("(a) Star Pattern")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n(b) Reverse Star Pattern")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\n(c) Number Pattern")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n(d) Reverse Number Pattern")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
