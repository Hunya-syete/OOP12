my_dict = {}

while True:
    print("\nWelcome, what would you like to do?")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

    choice = input("Enter your choice (a, b, c): ").lower()

    if choice == "a":
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        my_dict[key] = value
        print(f"Added: {key} - {value}")
    
    elif choice == "b":
        if not my_dict:
            print("Dictionary is empty. Cannot delete.")
        else:
            key_to_delete = input("Enter Key to delete: ")
            if key_to_delete in my_dict:
                del my_dict[key_to_delete]
                print(f"Deleted: {key_to_delete}")
            else:
                print(f"Key {key_to_delete} not found.")

    elif choice == "c":
        print("THANK YOU!")
        break

    else:
        print("Invalid choice. Please enter 'a', 'b', or 'c'.")
