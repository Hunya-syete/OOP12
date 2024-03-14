number = int(input("Enter a number for which you want to generate a multiplication table: "))

for i in range(1, 11):
 print(f"{number} x {i} = {number * i}")
