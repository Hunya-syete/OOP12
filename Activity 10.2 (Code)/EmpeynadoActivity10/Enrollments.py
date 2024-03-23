from Employee import employee
from Courses import courses

class enrollments:
    def __init__(self,grade,date):
        self.grade = grade
        self.date = date

    def enroll(self):
        print("Grade: ",self.grade, "\nDate: ",self.date)

class empEnrollments(employee):
    pass

class courseEnrollments(courses):
    pass

G1 = enrollments(98,"March 24, 2024")
G2 = enrollments(95,"March 24, 2024")
G3 = enrollments(88,"March 24, 2024")
G4 = enrollments(90,"March 24, 2024")



