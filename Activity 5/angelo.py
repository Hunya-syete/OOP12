num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

operator = input("Select Operator: (+,-,*,/)")

if  operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)

else:
    print("Invalid Input")
