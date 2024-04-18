from person import Person
from course import Course

class Trainer(Person):
    def __init__(self, firstName, lastName, phoneNumber, title, id, domain, salary):
        super().__init__(firstName, lastName, phoneNumber, title)
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def checkForRaise(self):
        if len(self.courses) >= 3:
            self.got_raise = True
            print(f"{self.firstName} {self.lastName} has received a raise.")

    def addCourse(self, course):
        self.courses.append(course)

    def printTrainerInfo(self):
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Title: {self.title}")
        print(f"ID: {self.id}")
        print(f"Domain: {self.domain}")
        print(f"Salary: {self.salary}")
        print("Courses:")
        for course in self.courses:
            print(f"- {course.name}")