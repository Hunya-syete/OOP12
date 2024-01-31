name = input("Enter Full Name:")
Math = int(input("Math grade: "))
Science = int(input("Science grade: "))
English = int(input("English grade: "))

Average = (Math + Science + English)/3

if Math < 73:
    if Average <= 73:
        print("Congratulations! " + name + " You passed the semester. But you need to re-enroll Math ")

if Science > 89:
    if Average >= 89:
        print("Congratulations! " + name + " You passed the semester ")

if English > 92:
    if Average >= 92:
        print("Congratulations! " + name + " You passed the semester ")
