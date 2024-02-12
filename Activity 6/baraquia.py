class Record:
    def __init__(self):
        self.records = {}

    def add_record(self, key , value):
        self.records[key] = value

    def view_records(self):
        print(self.records)

    def delete_record(self, key):
        if key in self.records:
            del self.records[key]
            print("Record deleted successfully.")
        else:
            print("Invalid key.")


record_keeper = Record()

while True:
    print("\n1. Add Data")
    print("2. Delete Data")
    print("3. End")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        record_keeper.add_record(key, value)
        record_keeper.view_records()
    elif choice == 2:
        key = input("Enter the key to delete: ")
        record_keeper.delete_record(key)
        record_keeper.view_records()
    elif choice == 3:
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
