Name = input("Name: ")
Math = int(input("Math grade: "))
Science = int(input("Science grade: "))
English = int(input("English grade: "))

Average = (Math + Science + English)/3


if Math < 75:
    if Average >= 75:
        print("Congratulations! " + Name + " You passed the semester. But you need to re-enroll Math.")


if Science < 75:
    if Average >= 75:
        print("Congratulations! " + Name + " You passed the semester. But you need to re-enroll Science.")


if English < 75:
    if Average >= 75:
        print("Congratulations! " + Name + " You passed the semester. But you need to re-enroll English.")


if Math >= 75 and Science >= 75 and English >= 75:
    if Average >= 75:
        print("Congratulations! " + Name + " You passed all the subjects for this semester.")

if Math < 75 and Science < 75 and English < 75:
    if Average < 75:
        print("Sorry, " + Name + " you failed this semester")
