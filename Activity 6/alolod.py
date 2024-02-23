dict = {}

print("What would you like to do?  \n a. Add Data \n b. Delete Data \n c. End")
userinput = input("Enter here:")

while True:

    if userinput == 'a':
        key = input("Please Enter Key: ")
        value = input("Please Enter Value: ")
        dict[key] = value
        print(f"Stored Data: {dict}")
        print("What would you like to do?  \n a. Add Data \n b. Delete Data \n c. End")
        userinput = input("Enter here:")

    if userinput == 'b':
        Rkey = input("Please Enter Key to Delete: ")
        del dict[Rkey]
        print(dict)
        print("What would you like to do?  \n a. Add Data \n b. Delete Data \n c. End")
        userinput = input("Enter here:")

    if userinput == 'c':
        print("Thank you for using this program! ".upper())
        break
