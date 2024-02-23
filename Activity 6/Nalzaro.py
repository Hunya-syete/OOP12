dict = {}

while True:
    print("Menu:")
    print("1. Add Data")
    print("2. Delete Data")
    print("3. End")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        dict[key] = value
        print("Data added successfully.")

    elif choice == "2":
        key_to_delete = input("Enter the key you want to DELETE: ")
        if key_to_delete in dict:
            del dict[key_to_delete]
            print("Data deleted successfully.")
        else:
            print("Key not found.")

    elif choice == "3":
        print("THANK YOU!")
        break
