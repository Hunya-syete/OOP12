UserInput = input("Enter ADD to Add data, DELETE to Delete data, END to Exit: ")
dict={}

if UserInput != "ADD" and UserInput != "DELETE" and UserInput!= "END":
    print("INVALID INPUT")

if UserInput == "ADD":
        Input1 = input("Enter Key: ")
        Input2 = input("Enter Value: ")
        dict[Input1] = Input2
        print(dict)
if UserInput == "END":
   print("Thank you")
   exit()

while "true":
    UserInput2 = input("Enter ADD to Add data, DELETE to Delete data, END to Exit: ")

    if UserInput2 != "ADD" and UserInput2 != "DELETE" and UserInput2 != "END":
        print("INVALID INPUT")

    if UserInput2 == "ADD":
        Input1 = input("Enter Key: ")
        Input2 = input("Enter Value: ")
        dict[Input1] = Input2
        print(dict)

    if UserInput2 == "DELETE":
        Input3 = str(input("Data you would like to delete?: "))
        del dict[Input3]
        print(dict)
    if UserInput2 == "END":
        print("Thank you")
        break;
