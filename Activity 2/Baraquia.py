def compute_average():
    name = input("Enter student's name: ")
    math = float(input("Enter Math grade: "))
    english = float(input("Enter English grade: "))
    science = float(input("Enter Science grade: "))
    
    average = (math + english + science) / 3
    
    if average >= 75:
        status = "Pass"
    else:
        status = "Fail"
    
    print(f"Student: {name}")
    print(f"Average: {average}")
    print(f"Status: {status}")

compute_average()
