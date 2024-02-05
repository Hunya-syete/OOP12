# Multiplication table
number = int(input("Enter a number: "))

for count in range(1, 11):
    product = number * count
    print(number, "*", count, "=", product)
