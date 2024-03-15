def add(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return x + y


def subtract(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return x - y


def multiply(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    return x * y


def divide(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    if y == 0:
        return "Error: Cannot divide by zero!"
    else:
        return x / y


def main():
    while True:
        print(
            'Hello! I am Poging Calculator created by Jaysever Hemoya. How can I assist you today with your '
            'calculations?')

        name = input("Please Enter your name: ")

        print("Welcome to Poging Calculator  {}!".format(name))
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid input")

        next_action = input("Select 'exit' to exit or press any other key to continue: \nthank you :) ")
        if next_action.lower() == 'exit':
            print("Exiting the calculator.")
            break


if "_main_":
    main()
