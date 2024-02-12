def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
        return "Error! Division by zero."
  
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1, 2, 3, 4, 5): ")

    if choice == '5':
        print("Exiting the calculator program.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    else:
        print("Invalid input! Please enter a valid choice.")
        continue

    print("Result: ", result)
```

This program defines functions for addition, subtraction, multiplication, and division. It then presents a menu to the user, takes input for the desired operation, and performs the calculation. The user can choose to exit the calculator by entering '5'.
