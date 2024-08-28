# match_case_calculator.py

# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user for the operation they'd like to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")
