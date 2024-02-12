rec_dict = {}

print("Choice an option:")
print("Add data")
print("Delete data")
print("Exit")

choice = input("Enter Your Choice (Add date, Delete data, Exit): ")

if choice == "Add data":
    key = input("Enter Key: Lastname: ")
    value = input(f"Enter value: ")
    rec_dict[key] = value
    print("Data add successfully.")
    print("Current record:", rec_dict)

if choice == "Delete data":
    key_to_delete = input("Enter key to delete: ")
    if key_to_delete in rec_dict:
        del rec_dict[key_to_delete]
        print(f"Data with key '{key_to_delete}' deleted.")
        print("Current records:", rec_dict)

    else:
        print(f"Key '{key_to_delete}' not found.")

elif choice == "Exit":
    print("Thank You and Have a Good Day!")
