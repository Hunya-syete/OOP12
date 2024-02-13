number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print("Please select operation:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n")

select = input(f"Select arithmetic operation (1/2/3/4): ")

def addition( number1, number2 ):
    return number1 + number2
def subtraction ( number1, number2 ):
    return  number1 - number2
def multiplication ( number1 , number2 ):
    return number1*number2
def division ( number1 , number2 ):
    return number1/number2

if select == "1":
    print(f"{number1} + {number2} = {addition(number1, number2)}")
if select == "2":
    print(f"{number1} - {number2} = {subtraction(number1, number2)}")
if select =="3":
    print(f"{number1} * {number2} = {multiplication(number1,number2)}")
if select =="4":
    print(f"{number1} / {number2} = {division(number1,number2)}")
else:
    print("Invalid input selection.")
