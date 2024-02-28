# program
Name = input("student name:")
math = float(input("math grade:"))
science = float(input("science grade:"))
english = float(input("english grade:"))

#calculate  the average
average =float(math + science + english) / 3

if math < 75:
 if average >= 75:
    print("Congrats! You passed the semester. But you need to re-enroll math subject.")


if science < 75:
 if average >= 75:
    print("Congrats! You passed the semester. But you need to re-enroll science subject.")

if english < 75:
 if average >= 75:
    print("Congrats! You passed the semester. But you need to re-enroll english subject.")


if math > 75 and science > 75 and english > 75:
    if average >= 75:
        print("Congrats! You passed all the subjects for this semester")

else:
    if math < 75 and science < 75 and english < 75:
     if average < 75:
        print("Sorry! You failed the semester")
