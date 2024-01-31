name = input("Enter student's name: ")
course = input("Enter your course: ")
year = input ("Enter your year: ")
math_grade = float(input("Enter math grade: "))
science_grade = float(input("Enter science grade: "))
english_grade = float(input("Enter english grade "))

average_grade = (math_grade + science_grade + english_grade) / 3

print(f"{name}'s average grade is: {average_grade:2f}")

if average_grade <(82): print("Soryy you have failed the semester.")
if average_grade >(82): print("Congratulations! You have passed the semester.")
if math_grade <float(82): print("Sorry you have to re-enroll the Math subject.")
if science_grade <float(82): print("Sorry you have to re-enroll the Science subject.")
if english_grade <float(82): print("Sorry you have to re-enroll the English subject.")
