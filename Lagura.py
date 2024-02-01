Name = input ("enter your  Name:")
math = int (input ( "Math"))
science = int ( input (" Science:"))
eng = int (input( "English"))
ave = int (math + science + eng) /3


if math <= int(99) and ave <= int (88) and science <= (92) and eng <= int (74)
   print ("Congratulations! You passed the semester, But you need to re-enroll English subject") 
    
if math <= int(75) and ave <= int(75) and science <= (75) and eng<=(75)
    

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
