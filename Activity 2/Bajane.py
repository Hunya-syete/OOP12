Name = str(input("Name:"))
math = float(input("MATH: "))
science = float(input("SCIENCE: "))
english = float(input("ENGLISH: "))
ave = (math + science + english)/3
print(ave)

if ave <=(72): print("sorry you have failed the semester")
if ave >=(79): print("Congratulations! you have passed the semester but you need to re-enroll in the subject")
if ave >=(80): print("you have passed the semester and you will proceed to the next semester")
if math <=float(72): print("sorry you have to re enroll in the subject of MATH")
if science <=float(73): print("sorry you have to re enroll in the subject of SCIENCE")
if english <=float(73): print("sorry you have to re enroll in the subject of ENGLISH")
