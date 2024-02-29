number = int(input("Enter then number of which user wants to print the multiplication table:"))

# We are using "for loop" to iterate the multiplication 10 times

print ("Multiplication table:", number)
for count in range(1,11):
    print(number, 'x', count, '=', number* count)
