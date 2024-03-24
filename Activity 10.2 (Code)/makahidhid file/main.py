from Person import person
from Address import Address
from Employee import Employee
from Trainer import Trainer
from Course import Course
from Enrollment import Enrollment



P1 = person("RICHARD", "MAKAHIDHID", "09068664066", "male")
P1.printfirstName()


A1 = Address("phillipine","dipolog city","upper turno","7100")
A1.printcountry()

E1 = Employee("GOVERMENT ID","MANAGER","NA","FEB 14 2022")
E1.printid()

T1 = Trainer("10,000","300","engineering","NA")
T1.printsalary()

C1 = Course("OOP","richard","JUMAWAN","next year")
C1.printsubject()

E2 = Enrollment("Technical Engineer","Computer Engineer","95","march 15 2024")
E2.printEmployee()

