from PersonMod import Person
from AddressMod import Address
from EmployeeMod import Employee, Enrollment, PartTime, Probation
from TrainerMod import Trainer, Courses, Raise
from Courses import Course, A_Trainer,A_Enrollment, Cancelled
from EnrollmentMod import E_Enrollment, E_Course, E_Employee,Grade

#PERSON
print("\n PERSON:")
Person1 = Person("Jhon", "Bicbic", "09998887777", "Student")
Person1.P_Person()

#ADDRESS
print("\n ADDRESS:")
Address1 = Address("Philippines", "Dipolog", "Biasong", "123")
Address1.P_Adress()

#EMPLOYEE
print("\n EMPLOYEE:")
Employee1 = Employee("123321", "Studentering", "03/16/2024", "Non")
enrolled = Enrollment()
enrolled.a_enroll("Studentering1")
enrolled.a_enroll("Studentering2")
enrolled.a_enroll("Studentering3")
PartTime1 = PartTime(False)
Probation1 = Probation(False)
Employee1.P_Employee()
enrolled.P_Enrollment()
PartTime1.P_PartTime()
Probation1.P_Probation()

#TRAINER
print("\n TRAINER:")
Trainer1 = Trainer("123321", "Google", "123", 1000)
courses = Courses()
courses.a_course("Studentering4")
courses.a_course("Studentering5")
Raise1 = Raise(True)
Trainer1.P_Trainer()
courses.P_Courses()
Raise1.P_Raise()

#COURSES
print("\n COURSES")
Course1 = Course("123321", "Studentering", "A12")
trainer2 = A_Trainer()
trainer2.a_trainer("Student Mastering1")
trainer2.a_trainer("Student Mastering2")
enrollment2 = A_Enrollment()
enrollment2.a_enroll("Student Mentoring1")
enrollment2.a_enroll("Student Mentoring3")
Cancelled1 = Cancelled(False)
Course1.P_Course()
trainer2.P_C_Trainer()
enrollment2.P_Enrollment()
Cancelled1.P_Cancelled()

#ENROLLMENT
print("\n ENROLLMENT")
Enrollment1 = E_Enrollment("03/19/2024")
grade1 = Grade()
grade1.a_grade(90)
Employee2 = E_Employee("444", "Studentering2", "03/18/2024", "Non")
Course2 = E_Course("55561", "Studentering3", "A6")
Enrollment1.P_Enrollment()
grade1.P_Grade()
Employee2.P_Employee()
Course2.P_Course()