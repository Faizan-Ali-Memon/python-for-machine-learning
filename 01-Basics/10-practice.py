# Practice: Applying Basics Together

import math

# --- VARIABLES ---
name = "Faizan"
age = 25
city = "Lahore"
print(f"Hi, I'm {name}, {age} years old from {city}.\n")

# --- STRINGS ---
quote = 'Python is a "powerful" programming language!'
print("Quote:", quote)
print("First 6 chars:", quote[:6])
print("Length of quote:", len(quote), "\n")

# --- CONDITIONALS ---
score = int(input("Enter your score (0–100): "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade, "\n")

# --- LOOPS ---
print("Multiples of 3 up to 20:")
for i in range(1, 21):
    if i % 3 == 0:
        print(i, end=" ")
print("\n")

# --- FUNCTIONS ---
def calculate_area(radius):
    return math.pi * radius ** 2

r = float(input("Enter radius: "))
print("Area of circle:", calculate_area(r), "\n")

# --- EXCEPTION HANDLING ---
try:
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))
    print("A divided by B =", a / b)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter valid integers.")
finally:
    print("Calculation attempt finished.\n")

# --- OPTIONAL: COMMAND-LINE-LIKE (interactive version here) ---
operation = input("Choose operation (add/subtract): ").lower()
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if operation == "add":
    print("Result:", num1 + num2)
elif operation == "subtract":
    print("Result:", num1 - num2)
else:
    print("Unsupported operation.")
