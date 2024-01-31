
Name = str(input("Name:"))
school = str(input("School:"))
course= str(input("Course:"))
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))
average = (math + science + english)/3
print(average)

if average <=(83): print("sorry you have failed the semester")
if average >=(84): print("Congratulations! you have passed the semester but you need to removal the subject")
if average >=(85): print("Congratulatios! you have passed the semester and you will proceed to the next semester")
if Math <=float(83): print("sorry you have to re enroll in the subject of Math")
if Science <=float(83): print("sorry you have to re enroll in the subject of Science")
if English <=float(83): print("sorry you have to re enroll in the subject of English")
