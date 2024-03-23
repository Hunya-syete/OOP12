from Employee import Employee
from Course import Course
from Trainer import Got_Raise

class Enrollment:
    def __init__(self, date):
        self.date = date

    def Date(self):
        print(self.date)

class Grade:
    def __init__(self, score):
        self.score = float(score)
        if self.score >= 90:
            print("Grade A")
        else:
            print("Grade B")

    def score(self):
        print(self.score)


class Employee23(Employee):
    pass


class got_raise(Got_Raise):
    pass


class Course23(Course):
    pass
