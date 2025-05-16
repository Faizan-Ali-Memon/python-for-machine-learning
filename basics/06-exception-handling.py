try:
    x = int(input("Enter number1: "))
    y = int(input("Enter number2: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid integers")
