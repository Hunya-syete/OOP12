def add(num1, num2):
    return int(num1) + int(num2)
def subtract(num1, num2):
    return int(num1) - int(num2)
def multiply(num1,num2):
    return int(num1) * int(num2)
def divide(num1, num2):
    return int(num1) / int(num2)

num1 = input("Input your First Number: ")
num2 = input("Input your Second Number: ")

print("Addition, Subtraction, Multiplication, Division")
operation = input("Input your desired Mathematical Operation: ")

if operation == "Addition":
    print(num1 + " + " + num2 + " = ", add(num1, num2))
elif operation == "Subtraction":
    print(num1 + " - " + num2 + " = ", subtract(num1, num2))
elif operation == "Multiplication":
    print(num1 + " * " + num2 + " = ", multiply(num1, num2))
elif operation == "Division":
    print(num1 + " / " + num2 + " = ", divide(num1, num2))
