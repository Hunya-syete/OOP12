number = float(input("Enter number: "))
print("Multiplication table of:", number)
for count in range(1,11):
    print(number, "*", count, "=", number* count)
