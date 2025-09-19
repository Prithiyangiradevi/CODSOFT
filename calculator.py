# CODSOFT Internship - Task 2 (Calculator)
# Author: Prithiyangira Devi
# Project: Calculator
print("👋 Welcome to Your Friendly Calculator!")
print("I can help you add, subtract, multiply, or divide two numbers.")

# Function to get a number from the user
def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Oops! That doesn't look like a number. Try again.")

# Function to get the operation choice from the user
def get_operation():
    print("\nChoose an operation:")
    print("1 ➕ Addition")
    print("2 ➖ Subtraction")
    print("3 ✖️ Multiplication")
    print("4 ➗ Division")
    
    while True:
        choice = input("Enter 1, 2, 3, or 4: ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Hmm, that's not a valid choice. Please choose again.")

# Get user input
num1 = get_number("\nEnter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

# Perform calculation
if operation == '1':
    result = num1 + num2
    symbol = '+'
elif operation == '2':
    result = num1 - num2
    symbol = '-'
elif operation == '3':
    result = num1 * num2
    symbol = '×'
elif operation == '4':
    if num2 == 0:
        result = "Error! Division by zero is not allowed."
        symbol = '/'
    else:
        result = num1 / num2
        symbol = '/'

# Display result
print(f"\nResult: {num1} {symbol} {num2} = {result}")
print("\nThanks for using the calculator! 😄")
