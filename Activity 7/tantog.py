# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Getting user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Choosing an operation
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter the operation number (1/2/3/4): ")

# Performing the operation and displaying the result
if operation == "1":
    print("The result of the addition is:", add(num1, num2))
elif operation == "2":
    print("The result of the subtraction is:", subtract(num1, num2))
elif operation == "3":
    print("The result of the multiplication is:", multiply(num1, num2))
elif operation == "4":
    print("The result of the division is:", divide(num1, num2))
else:
    print("Invalid operation number! Please try again.")
