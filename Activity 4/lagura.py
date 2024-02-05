number = int(input ("Enter then number of which the user wants to print the multiplication table:"))
# We are using "for loop" to iterate the multiplication 10 times
print ("The Multiplication table of:", number)
for count in range(1,10):
    print (number, '*', count, '=', number* count)
