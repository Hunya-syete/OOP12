#Multiplication table
number = (input("Enter the number of which the user wants to print the multiplication table:"))
print("The multiplication table of:", number)
for count in range(1, 11):
    result = number = count
    print (number, 'x', count, '=', result)
