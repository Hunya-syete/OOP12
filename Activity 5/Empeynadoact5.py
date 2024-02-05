number2 = int(input("Enter second number: " ))
operation= input("Please select from the following(Addition,Subtraction,Multiplication,Division): ")

Addition = number1 + number2
Subtraction = number1 - number2
Multiplication = number1 * number2
Division = number1 / number2

if operation == "Addition":
    print(str(number1) + "+" + str(number2) + "=" + str(Addition))
if operation == "Subtraction":
    print(str(number1) + "-" + str(number2) + "=" + str(Subtraction))
if operation == "Multiplication":
    print(str(number1) + "*" + str(number2) + "=" + str(Multiplication))
if operation == "Division":
    print(str(number1) + "/" + str(number2) + "=" + str(Division))
