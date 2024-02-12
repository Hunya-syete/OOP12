user_number = int(input("Enter a number: "))
user_number2 = int(input("Enter another number: "))
arithmetic_op = input(f"What arithmetic operation do you want to use? Addition, Subtraction, Multiplication, Division: ")

def add():
    return user_number + user_number2

def subtract():
    return user_number - user_number2

def multiply():
    return user_number * user_number2

def divide():
    return user_number / user_number2

if arithmetic_op == "Addition":
    print(add())
elif arithmetic_op == "Subtraction":
    print(subtract())
elif arithmetic_op == "Multiplication":
    print(multiply())
elif arithmetic_op == "Division":
    print(divide())
