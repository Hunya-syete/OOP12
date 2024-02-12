def calculator():
    print("Simple Calculator")
    num3, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")


    if operation == '+':
        result = num3 + num2
    if operation == '-':
        result = num3 - num2
    if operation == '*':
        result = num3 * num2
    if operation == '/':
        result = num3 / num2 if num2 != 0 else "Error: Division by zero"

        print("Invalid operation. Please choose +, -, *, or /.")

    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
