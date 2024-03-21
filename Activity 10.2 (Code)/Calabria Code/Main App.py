from Course import Course
from Person import Person
from Address import Address
from Employee import Employee, enrollment, parttime, probation
from Trainer import Trainer, Raise
from Enrollment import Enrollment

#PERSON
print("\nPERSON:")
Person1 = Person("Mc Alexis", "Calabria", "09998887777", "Student")
Person1.fullname()

#ADDRESS
print("\nADDRESS:")
Address1 = Address("Philippines", "Dipolog", "Turno", "7100")
Address1.display()

print("\nEMPLOYEE:")
Employee1 = Employee("McEgglok", "Computer Engineering", "Non", "7-15-23")
Employee1.information()
enroll = enrollment()
enroll.enroll1("Studentering1")
enroll.enroll1("Studentering2")
enroll.enroll1("Studentering3")
PartTime1 = parttime(False)
Probation1 = probation(False)
enroll.Enrollment2()
PartTime1.PartTime1()
Probation1.Probation1()

print("\nTRAINER:")
Trainer1 = Trainer("123321", "Google", 1000)
Trainer1.train()
Raise1 = Raise(True)
Raise1.Raise()

print("\nCOURSES")
Course1 = Course("Mcegglok2345", "Computer Engineering", "Non", "7-15-23" )
Course1.course1()
enroll = enrollment()
enroll.enroll1("Studentering1")
enroll.enroll1("Studentering2")
enroll.enroll1("Studentering3")
PartTime1 = parttime(False)
Probation1 = probation(False)
enroll.Enrollment2()
PartTime1.PartTime1()
Probation1.Probation1()

print("\nENROLLMENT")
Enrollment2 = Enrollment("Mc Alexis", "Calabria", "none")
Enrollment2.enrollment1()
