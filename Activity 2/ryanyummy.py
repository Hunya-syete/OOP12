name = input("Enter Full Name: ")
Math = float(input("Math grade: "))
Science = float(input("Science grade: "))
English = float(input("English grade: "))

average = (Math + Science + English) / 3

print(f"{name}'s average grade is {average:2f}.")

if average<= (75): print("you failed to passed the semester")
if average >=(75): print("Congratulations! You passed the semester")
if average >= (85): print("Sorry you failed this subject ")
if Math >=float(85): print("Sorry you failed this subject ")
if Science >=float(85): print("Sorry you failed this subject ")
if English >=float(85): print("Sorry you failed this subject ")
