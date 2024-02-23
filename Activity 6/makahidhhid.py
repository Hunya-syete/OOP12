dict = {}

print("\nwelcome,choose a option:")
print("a. add data")
print("b. delete data")
print("c. exit")

choice = input("enter your choice: ")
key = input("enter key:Lastname:")
value = input(f"enter value:")
if choice == "a":
    dict[key] = value
    print(dict)

elif choice == "b":
    dict[key] = value
    print(dict)

elif choice == "c":
    print("thank you for")
    exit
