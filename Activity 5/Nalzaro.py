Operation: str = input("Enter an operator (Addition, Subtraction, Multiply, Division): ")
a = float(input("Enter the First Number: "))
y = float(input("Enter the Second Number: "))

print(f"Operator: {Operation}")
print(f"First Number: {a}")
print(f"Second Number: {y}")
print("Answer:")

if Operation == "Addition":
    result = a + y
    print(round(result, 3))
elif Operation == "Subtraction":
    result = a - y
    print(round(result, 3))

elif Operation == "Multiply":
    result = a * y
    print(round(result, 3))
elif Operation == "Division":
    result = a / y
    print(round(result, 3))
else:
    print(f"{Operation} is not a valid operator")
