# Define for basic arithmetic operations
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y != 0:
    return x / y
  else:
    return "Cannot divide by zero"

# User input for to number and operation
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
operator = input("Select Operator: (+,-,*,/)")

# Perform the corresponding operation
if  operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    result = "Invalid Operation"
