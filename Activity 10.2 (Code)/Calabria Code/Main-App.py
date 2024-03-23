from Course import Course
from Person import Person
from Address import Address
from Employee import Employee, enrollment, parttime
from Trainer import Trainer, Got_Raise, Salary
from Enrollment import Enrollment, Grade

# PERSON MODULE
print("\nPERSON:")
# (firstname: string), (lastname: string), (phoneNumber: string), (titile: string)
Person1 = Person("Mc Alexis", "Calabria", "09998887777", "Student")
Person1.fullname()
# addAddress()
Address2 = Address("\nPhilippines", "Dipolog", "Turno", "7100")
Address2.display()

# ADDRESS MODULE
print("\nADDRESS:")
# (country: string), (city: string), (street: string), (postal code: string)
Address1 = Address("Philippines", "Dipolog", "Turno", "7100")
Address1.display()

# EMPLOYEE MODULE
print("\nEMPLOYEE:")
# (id: string), (title: string), (international: string), (dateofemployment: string)
Employee1 = Employee("246", "Computer Engineering", "Filipino", "6-15-5")
Employee1.information()
# (Enroll: list)
enroll = enrollment()
enroll.enroll1("\nStudentering1")
enroll.enroll1("Studentering2")
enroll.enroll1("Studentering3")
enroll.Enrollment2()
# (isparttime(): Boolean)
PartTime = parttime(True)
PartTime.parttime1()

# TRAINER MODULE
print("\nTRAINER:")
# (id: string), (domain: string)
Trainer1 = Trainer("123", "CEO")
Trainer1.train()
# (salary: float)
Salary1 = Salary(90)
print(Salary1.salary)
# got_raise(): Boolean
Raise1 = Got_Raise(True)
Raise1.gotraise()
# addAddress()
Address3 = Address("\nPhilippines", "Dipolog", "Turno", "7100")
Address3.display()

# COURSE MODULE
print("\nCOURSE")
# (id: string), (title: string), (international: string), (dateofemployment: string)
Course1 = Course("12345", "Computer Engineering", "Filipino", "6-15-5")
Course1.course1()
# (Enroll: list)
enroll = enrollment()
enroll.enroll1("\nStudent Mentor1")
enroll.enroll1("Student Mentor2")
enroll.enroll1("Student Mentor3")
enroll.Enrollment2()
# (isparttime(): Boolean)
PartTime1 = parttime(True)
PartTime1.parttime1()

# ENROLLMENT MODULE
print("\nENROLLMENT:")
# grade: float
Grade1 = Grade(80)
print(Grade1.score)
# date: date
Enrollment1 = Enrollment("7-15-23")
Enrollment1.Date()
# Employee: Employee
Employee1 = Employee("\nMc123", "Computer Engineering", "Filipino", "6-15-5")
Employee1.information()
# CheckforRaise()
Raise1 = Got_Raise(True)
Raise1.gotraise()
# addCourses()
Course1 = Course("\nAlexis123", "Teacher", "Filipino", "6-15-5")
Course1.course1()
