Chosen_number = float(input("Enter a number to be multiplied: "))

print(f"Chosen Number: {Chosen_number}")
print(f"Multiplication table of: {Chosen_number} to x10")
for count in range(1,11):
    print(Chosen_number, "X" , count, "=", Chosen_number* count)
