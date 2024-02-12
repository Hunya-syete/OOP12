def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
    return"error:division by zero"
def main():
 print("welcome to the simple calculator program")

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

operation = input("enter the operation (+,-,*,/):")

if operation == "+":
    print("result:",addition(number1,number2))
elif operation == "-":
    print("result:",subtraction(number1,number2))
elif operation == "*":
    print("result:",multiplication(number1,number2))
elif operation == "/":
    print("result:",division(number1,number2))
    print("invalid operation entered.")

if __name__ == '__main__':
    main()
