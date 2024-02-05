# Generate a number
num = int(input("Enter a Number: "))

# Generate and Print Multiplication table
print("Multiplication table for {num}:")
for i in range(1,10):
    result = num * i
    print(f"{num} x {i} = {result}")
