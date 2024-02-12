def display_menu():
    print("==========================================")
    print("         ~ Record Keeping App ~")
    print("==========================================")
    print("Available Options:")
    print("1.) Add Data\t\t2.) Delete Data")
    print("3.) End\t4.) Exit App\n")
    print()

def add_record(file):
    var1 = input("Enter Name: ")
    var2 = input("Enter Email: ")
    var3 = input("Enter Address: ")
    file.write(f"{var1}, {var2}, {var3}\n")

def view_records(file):
    if file.read().strip() == "":
        print("No records found.")
    else:
        print(file.read())

def clear_records(file):
    file.seek(0)
    file.truncate()
    print("All records cleared.")

def main():
    file = open("records.txt", "a+")
    file.seek(0)

    while True:
        display_menu()
        selection = input("Select an option [A,B,C,D]: ").upper()

        if selection == "A":
            add_record(file)
        elif selection == "B":
            view_records(file)
        elif selection == "C":
            clear_records(file)
        elif selection == "D":
            print("Thank you")
            file.close()
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
    print("==========================================")
    print("         ~ Record Keeping App ~")
    print("==========================================")
    print("Available Options:")
    print("A) Add Record\t\tB) View Records")
    print("C) Clear Records\tD) Exit App\n")
    print()

def add_record(file):
    var1 = input("Enter Name: ")
    var2 = input("Enter Email: ")
    var3 = input("Enter Address: ")
    file.write(f"{var1}, {var2}, {var3}\n")

def view_records(file):
    if file.read().strip() == "":
        print("No records found.")
    else:
        print(file.read())

def clear_records(file):
    file.seek(0)
    file.truncate()
    print("All records cleared.")

def main():
    file = open("records.txt", "a+")
    file.seek(0)

    while True:
        display_menu()
        selection = input("Select an option [A,B,C,D]: ").upper()

        if selection == "A":
            add_record(file)
        elif selection == "B":
            view_records(file)
        elif selection == "C":
            clear_records(file)
        elif selection == "D":
            print("Thank you")
            file.close()
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
