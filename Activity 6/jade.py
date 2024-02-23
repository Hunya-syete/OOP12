# introduction
dict_data = {}

print("Welcome! What would you like to do?")
print("a. Add Data")
print("b. Delete Data")
print("c. End")

while True:
    choice = input("What would you like to do?: ").lower()

# choices code
    if choice == "a":
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        dict_data[key] = value
        print("Data added successfully:", dict_data)

    elif choice == "b":
        key_to_delete = input("Enter the key you want to DELETE: ")
        if key_to_delete in dict_data:
            del dict_data[key_to_delete]
            print("Data deleted successfully:", dict_data)
        else:
            print("Key not found. Please enter a valid key.")

    elif choice == "c":
        print("THANK YOU!")
        break
# Invalid
    else:
        print("Invalid choice. Please choose 'a', 'b', or 'c'.")
