number = int(input("Enter then number of which the user wants to print the multiplication table:"))
count = 1
# We are using "for loop " to iterating the multiplication  10 times
print ("The Multiplication table of:", number)
while count in range(1,10):
   number = number *1
   print (number,'x', count,'=', number* count)
   count+=1
