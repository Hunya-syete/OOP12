from person import Person
from address import Address
from employee import Employee
from course import Course
from trainer import Trainer
from enrollment import Enrollment
from datetime import date


person1 = Person("Thro", "Cortz", "09706157078", "Mr.")
person1.addAddress(Address("USA", "New York", "123 Main St", "10001"))
date_of_employment = (2021, 1, 1)

employee = Employee("Kloi", "Cabz", "0930070275", "Mr.", "E001", True, True,date_of_employment)



course1 = Course("C001", "Python Programming", "PY101", 20)

trainer1 = Trainer("Bob", "Johnson", "994-3985-654", "Mr.", "T001", "IT", 50000.0)

enrollment1 = Enrollment(employee, course1, None, date(2024, 3, 22))

course1.addTrainer(trainer1)
course1.addEnrollment(enrollment1)
employee.addEnrollment(course1)
print("Person 1:")
person1.printPersonInfo()
print("\nEmployee 1:")
employee.printEmployeeInfo()
print("\nTrainer 1:")
trainer1.printTrainerInfo()
print("\n")
enrollment1.printEnrollmentInfo()