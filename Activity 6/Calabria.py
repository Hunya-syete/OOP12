dict = []

def add_record():
    name = input("Enter name: ")
    address = input("Enter address: ")
    dict.append({"name": name, "address": address})
    print("Record added.\n")

def view_records():
    if not dict:
        print("No records found.\n")
    else:
        for index, record in enumerate(dict, start=1):
            print(f"Record {index}:")
            print(f"Name: {record['name']}")
            print(f"Address: {record['address']}\n")

def clear_records():
    global dict
    dict.clear()
    print("All records cleared.\n")

def main():
    while True:
        print("Record Keeping App")
        print("(Add) Add Record")
        print("(View) View Records")
        print("(Delete) Delete Records")
        print("(End) Exit App\n")

        try:
            selection = input("Select an option [Add,View,Delete,End]: ")
        except KeyboardInterrupt:
            print("\nExiting app...")
            exit()

        if selection == "Add":
            add_record()
        elif selection == "View":
            view_records()
        elif selection == "Delete":
            clear_records()
        elif selection == "End":
            print("Thank you.")
            break
        else:
            print("Invalid input.\n")

if __name__ == "__main__":
    main()
