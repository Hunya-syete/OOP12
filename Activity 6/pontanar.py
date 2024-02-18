record = {}

def add_record():
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    record[key] = value

def delete_record():
    key = input("Enter the Key you want to delete: ")
    if key in record:
        del record[key]
        print(f"Key {key} deleted successfully.")
    else:
        print(f"Key {key} not found.")

def main():
    while True:
        choice =\
            input("Enter ADD data, DELETE data, END: ")
        if choice == "ADD":
            add_record()
        elif choice == "DELETE":
            delete_record()
        elif choice == "END":
            print("Thank you.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
