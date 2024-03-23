from Person import P1
from Person import P2
from Person import P3
from Person import P4
from Person import P5
from Person import P6
from Address import Add1
from Address import Add2
from Address import Add3
from Address import Add4
from Address import Add5
from Address import Add6
from Employee import E1
from Trainer import T1
from Trainer import T2
from Courses import C1
from Courses import C2
from Enrollments import G1
from Enrollments import G2


a = input("Choose from the Student ff(Student,Employee,Trainer): ")

if a == "Student" and "student":
    b = input("Last name: ")
    if b == "Cortez":
        P1.printPerson()
        Add1.printAdd()
    if b == "Bicbic":
        P2.printPerson()
        Add2.printAdd()

if a == "Employee" and "employee":
    c = input("Id of Employee: ")
    if c == "125982":
        P3.displayPerson()
        E1.displayEmployee()
        Add3.printAdd()
        G1.enroll()
    if c == "125662":
        P4.displayPerson()
        E1.displayEmployee()
        Add4.printAdd()
        G2.enroll()
    d = int(input("Working for how many months? "))
    if d <= 2:
        print("Employee Status: OJT")
    if d >=3 and d <= 6:
        print("Employee Status: Probationary")
    if d > 6:
        print("Employee Status: Regular")

if a == "Trainer" and "trainer":
    e = input("Id of Trainer: ")
    if e == "256489":
        P5.displayPerson()
        T1.displayTrainer()
        Add5.printAdd()
        C1.coursesDisplay()
    if e == "256897":
        P6.displayPerson()
        T2.displayTrainer()
        Add6.printAdd()
        C2.coursesDisplay()







