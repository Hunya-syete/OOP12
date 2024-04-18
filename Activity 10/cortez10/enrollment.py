class Enrollment:
    def __init__(self, employee, course, grade, date):
        self.employee = employee
        self.course = course
        self.grade = grade
        self.date = date

    def setGrade(self, grade):
        self.grade = grade

    def printEnrollmentInfo(self):
        print(f"Employee: {self.employee.firstName} {self.employee.lastName}")
        print(f"Course: {self.course.name}")
        print(f"Grade: {self.grade}")
        print(f"Date: {self.date}")