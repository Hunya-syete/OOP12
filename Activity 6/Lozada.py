def add_data(data):
    key = input("Enter key: ").strip().lower()
    value = input("Enter value: ").strip()
  
    if key in data:
        print(f"Key '{key}' already exists. Do you want to overwrite the value? (yes/no)")
        if not input().strip().lower() == "yes":
            return

    data[key] = value
    print(f"Added: ({key.capitalize()}: {value})")


def delete_data(data):
    key = input("Enter key to delete: ").strip().lower()
    if key not in data:
        print("Key not found.")
        return

    del data[key]
    print("Data deleted successfully.")


def display_data(data):
    print("\nData:")
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")


def main():
    print("Record Keeping App")
    data = {}

    while True:
        print("\n1. Add data")
        print("2. Delete data")
        print("3. Display data")
        print("4. End")

        choice = input("Enter your choice: ").strip().lower()

        if choice in {"1", "add data"}:
            add_data(data)
        elif choice in {"2", "delete data"}:
            delete_data(data)
        elif choice in {"3", "display data"}:
            display_data(data)
        elif choice in {"4", "end"}:
            print("Thank you for using the app!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
