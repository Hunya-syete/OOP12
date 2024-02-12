def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_operation_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def perform_operation(choice, num1, num2):
    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == 4:
        try:
            print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError as e:
            print(e)
            return

def main():
    choice = get_operation_choice()
    num1, num2 = get_numbers()
    perform_operation(choice, num1, num2)

if __name__ == "__main__":
    main()
