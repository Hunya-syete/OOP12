Name = input("Enter full name:")
Math = int(input("Enter Math grade: "))
Science = int(input("Enter Science grade: "))
English = int(input("Enter English grade: "))

Average = (Math + Science + English)/3

if Average > 74:
    print("Your average is " + str(Average) + " You passed the semester")

if Average <= 74:
    print("Your average is " + str(Average) + " You failed the semester")


if Math <= 74:
    print("and you need to re enroll Math")

if Science <= 74:
    print("and you need to re enroll Science")

if English <= 74:
    print("and you need to re enroll English")
