from Person import Person
from Address import Address
from Employee import Employee
from Trainor import Trainor
from Course import Course
from Enrollment import Enrollment

# Creating instances memory data
person1 = Person("Angelo", 19, "Male")
person2 = Person("Ana", 20, "Female")

address1 = Address("Magsaysay St", "Dipolog", 7100)
address2 = Address("Rizal St", "Dipolog City", 7100)

employee1 = Employee("Eva", 27, "Female", 34488)
employee2 = Employee("Franky", 31, "Male", 291177)

trainor1 = Trainor("Mary", 32, "Female", 144635)
trainor2 = Trainor("Vincel", 38, "Female", 554135)

course1 = Course(202306, "Computer Engineering")
course2 = Course(202362, "Civil Engineering")

enrollment1 = Enrollment(202318, 202306)
enrollment2 = Enrollment(202304, 202362)

# Information data
print("Person 1:", person1.name, ",", person1.age, ",", person1.gender)
print("Person 2:", person2.name, ",", person2.age, ",", person2.gender)
print("")
print("Address 1:", address1.street, ",", address1.city, ",", address1.zip_code)
print("Address 2:", address2.street, ",", address2.city, ",", address2.zip_code)
print("")
print("Employee 1:", employee1.name,",", employee1.age, ",", employee1.gender, ",", employee1.employee_id)
print("Employee 2:", employee2.name,",", employee2.age, ",", employee2.gender, ",", employee2.employee_id)
print("")
print("Trainor 1:", trainor1.name, ",", trainor1.age, ",", trainor1.gender, ",", trainor1.trainor_id)
print("Trainor 2:", trainor2.name, ",", trainor2.age, ",", trainor2.gender, ",", trainor2.trainor_id)
print("")
print("Course 1", course1.course_id, ",", course1.title)
print("Course 2", course2.course_id, ",", course2.title)
print("")
print("Enrollment 1:", enrollment1.employee_id, ",", enrollment1.course_id)
print("Enrollment 2:", enrollment2.employee_id, ",", enrollment2.course_id)