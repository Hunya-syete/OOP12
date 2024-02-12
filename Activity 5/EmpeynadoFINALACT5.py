
print("Hello, Welcome to the world of Mathematics")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter second number: "))
operation = input("Please select from the following(Addition,Subtraction,Multiplication,Division): ")

def Addition(number1,number2):
    return int(number1) + int(number2)
def Subtraction(number1,number2):
    return int(number1) - int(number2)
def Multiplication(number1,number2):
    return int(number1) * int(number2)
def Division(number1,number2):
    return int(number1) / int(number2)

if operation == "Addition":
    print(str(number1) + "+" + str(number2) + "=" + str(Addition(number1,number2)))
if operation == "Subtraction" and number2 <= number1:
    print(str(number1) + "-" + str(number2) + "=" + str(Subtraction(number1,number2)))
if operation == "Multiplication":
    print(str(number1) + "*" + str(number2) + "=" + str(Multiplication(number1,number2)))
if operation == "Division" and number2 <= number1:
    print(str(number1) + "/" + str(number2) + "=" + str(int(number1) / int(number2)))

if operation == "Subtraction" and number2 > number1:
    print("Second number cannot be larger than first number")
if operation == "Division" and number2 > number1:
    print("Second number cannot be larger than first number")
