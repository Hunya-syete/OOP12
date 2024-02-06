def addition(number1,number2):
    return number1 + number2

def subtraction(number1,number2):
    return number1 - number2

def multiplication(number1,number2):
    return number1 * number2

def division(number1 , number2):
    return number1 / number2

print("Please select operation:/n"
      "1.Addition/n"
      "2.Subtraction/n"
      "3.Multiplication/n"
      "4.Division/n"
      "5.Exit/n")

select = int(input("Select operation (1/2/3/4):"))
number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

if select == 1:
    print(f"{number_1}  + {number_2} = {addition(number_1,number_2)}")

elif select == 2:
    print(f"{number_1}  - {number_2} = {subtraction(number_1,number_2)}")

elif select == 3:
    print(f"{number_1}  * {number_2} = {multiplication(number_1, number_2)}")

elif select == 4:
    print(f"{number_1}  / {number_2} = {division(number_1, number_2)}")

else:
    print("Invalid input.")

    print("Result:,result")
