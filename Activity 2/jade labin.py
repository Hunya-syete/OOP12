# import library sys for exit function


# get single input from console
print("")
print("---STUDENT INFORMATION---")
jmdStudNo = str(input("Enter student number:  "))
jmdFtudName = str(input("Enter First name:  "))
jmdLtudName = str(input("Enter Last Name  "))
print("")

# display course code + course description
print("Choose Course Code")
print("[1] BSCPE")
print("")
#Get the selected Information
jmdChoice = int(input("Enter Course Code: "))
print("")

# get single input from console
print("")
math = float(input("MATH: "))
science = float(input("SCIENCE: "))
english = float(input("ENGLISH: "))
ave = (math + science + english)/3
print(ave)

if ave <=(74): print("sorry you have failed the semester")

if ave >=(75): print("Congratulations you have succeeded and you have passed the semester but you need to re-enroll in the subject")

if ave >=(82): print("you have passed the semester and you will proceed to the next semester")

if math <=float(74): print("sorry you have to re enroll in the subject")

if science <=float(74): print("sorry you have to re enroll in the subject")

if english <=float(74): print("sorry you have to re enroll in the subject")
