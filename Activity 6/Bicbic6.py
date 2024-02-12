dict = {}

print("Welcome, what would you like to do?")
print("a. Add Data")
print("b. Delete Data")
print("c. End")

while True:
    Choice1 = input("What would you like to do?: ")
    if Choice1 == "a":
        Key = input("Enter Key: ")
        Value = input("Value: ")
        dict[Key] = Value
        print(dict)

    if Choice1 == "b":
        Choice2 = str(input("What index would you like to DELETE?: "))
        del dict[Choice2]
        print(dict)

    if Choice1 == "c":
        print("THANK YOU!")
        break;