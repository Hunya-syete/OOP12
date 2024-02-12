user_number = int(input("[Enter number:] "))
user_number2 = int(input("[Enter another number:] "))
arithmetic_op = input("Which arithmetic operation do you want to use? Subtraction, Multiplication, Addition, Division: ")

def subtract():
    return user_number - user_number2

def multiply():
    return user_number * user_number2

def add():
    return user_number + user_number2

def divide():
    if user_number2 == 0:
        return "Error: Division by zero"
    else:
        return user_number / user_number2

if arithmetic_op == "Subtraction":
    print(subtract())
elif arithmetic_op == "Multiplication":
    print(multiply())
elif arithmetic_op == "Addition":
    print(add())
elif arithmetic_op == "Division":
    print(divide())
else:
    print("Invalid arithmetic operation selected")
