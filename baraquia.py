name = input ("enter your  Name:")
math = float (input ( "Math"))
science = float ( input (" Science:"))
eng = float (input( "English"))
ave = float (math + science + eng) /3


if math <= float(99) and ave <= float (88) and science <= (92) and eng <= float (74)
   print ("Congratulations! You passed the semester, But you need to re-enroll English subject") 
    
if math <= float(75) and ave <= float(75) and science <= (75) and eng<=(75)
    

if math<75:
    if ave >= 75:
        print("Congratulations!  You passed the semester, But you need to re-enroll Math subject")

if eng < 75:
    if ave >= 75:
        print("Congratulations!  You passed the semester, But you need to re-enroll eng subject")

if science < 75:
    if ave >= 75:
        print("Congratulations!  You passed the semester, But you need to re-enroll science subject")

if ave < 75:
        print("Congratulations!  You passed the semester, But you need to re-enroll the subject")

else:
    print("Sorry! you failed this semester")
