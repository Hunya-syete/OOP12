name = input("Enter fullname: ")
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))
average = (math + science + english)/3

print(average)
if math < float(74) and average >= float(75) and science >= float(75) and english >= float(75):
    print("Congratulations! You passed the semester. But please re-enroll Math subject.")

if math < float(74) and science <= float(74) and english <= float(74) and average >= float(75):
    print("Sorry! You failed to pass the semester.")

if science < float(74) and average >= float(75) and math >= float(75) and english >= float(75):
    print("Congratulations! You passed the semester. But please re-enroll Science subject.")

if science < float(74) and math <= float(74) and english <= float(74) and average >= float(75):
    print("Sorry! You failed to pass the semester.")

if english < float(74) and average >= float(75) and math <= float(75) and science <= float(75):
    print("Congratulations! You passed the semester. But please re-enroll English subject.")

if english < float(74) and math <= float(74) and science <= float(74) and average >= float(75):
    print("Sorry! You failed to pass the semester.")

if average > float(75) and math >= float(75) and science >= float(75) and english >= float(75):
    print("Congratulations! You passed the semester. You may proceed to the second semester.")

if average < float(74) and math <= float(74) and science <= float(74) and english <= float(74):
    print("Sorry! You failed to pass this semester.")
