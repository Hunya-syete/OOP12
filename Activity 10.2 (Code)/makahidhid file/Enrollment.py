
class Enrollment:
    def __init__(self,employee,course,grade,date):
        self.employee = employee
        self.course=course
        self.grade = grade
        self.date = date

    def printEmployee(self):
        print(self.employee,self.course,self.grade,self.date)


