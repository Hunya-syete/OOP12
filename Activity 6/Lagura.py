myDict = {}
print("please select the following: [a]: Add Data, [d]: for delete Data, [e]:  to end")

for i in iter(int, 1):
    c = input("Enter your choice: ")
    if (c == "a") :
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        
        print("Record Deleted successfully.'")
    else:
        print("Invalid key.")
        
record_keeper = input
myDict = {}
while True:
    print("a. Add Data")
    print("d. Delete Data")
    print("e. End")

    a, d, e = int(input("Enter your choice: "))

    if a == a:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        record_keeper.add_Data(key, value)
        record_keeper.view_Data()
    elif d == d:
        key = input("Enter the key to delete: ")
        record_keeper.delete_Data(key)
        record_keeper.view_Data()
    elif e == e:
        print("THANK YOU")
       
    else:
        print("Invalid choice. Please choose a valid option.")
