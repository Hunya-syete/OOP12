from person import Person
from course import Course
from enrollment import Enrollment
from datetime import datetime, timedelta, date


class Employee(Person):
    def __init__(self, firstName, lastName, phoneNumber, title, id, international, field, dateOfEmployment):
        super().__init__(firstName, lastName, phoneNumber, title)
        self.id = id
        self.international = international
        self.field = field
        self.dateOfEmployment = dateOfEmployment
        self.enrolled = []

    def addEnrollment(self, course):
        self.enrolled.append(course)

    def isPartTime(self):
        return self.field

    def printEmployeeInfo(self):
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Title: {self.title}")
        print(f"ID: {self.id}")
        print(f"International: {self.international}")
        print(f"Part-Time: {Employee.isPartTime(self)}")
        print(f"Field: {self.field}")
        print(f"Date of Employment: {self.dateOfEmployment}")