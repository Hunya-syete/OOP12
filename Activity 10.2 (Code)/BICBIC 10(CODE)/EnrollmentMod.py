from EmployeeMod import Employee
from Courses import Course

class E_Enrollment:
    def __init__(self, date):
        self.date = date

    def P_Enrollment(self):
        print("\n", self.date)

class Grade:
    def __init__(self):
        self.grade = float()

    def a_grade(self, a_grade=0):
        self.grade += a_grade

    def P_Grade(self):
        print("",self.grade)

class E_Employee(Employee):
    pass

class E_Course(Course):
    pass