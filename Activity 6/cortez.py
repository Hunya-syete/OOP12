print("How can I help you? Please choose a key.  \n 1. Add Data \n 2. Delete Data \n 3. End")
userinput = input("Enter here:")

while True:

    if userinput == '1':
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        dict[key] = value
        print(f"Stored Data: {dict}")
        print("How can I help you? Please choose a key.  \n 1. Add Data \n 2. Delete Data \n 3. End")
        userinput = input("Enter here:")

    if userinput == '2':
        recordkey = input("Please Enter Key to Delete: ")
        del dict[recordkey]
        print(dict)
        print("How can I help you? Please choose a key.  \n 1. Add Data \n 2. Delete Data \n 3. End")
        userinput = input("Enter here:")

    if userinput == '3':
        print("THANK YOU")
        break
