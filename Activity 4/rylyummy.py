user = input("Enter name: ")
number = int(input("Enter the number of your desired Multiplication table: "))
count = 1
print("The Multiplication Table of: ", number)

while count <= 10:
    number = number * 1
    print(number, "*", + count, "=", number * count)
    count += 1
