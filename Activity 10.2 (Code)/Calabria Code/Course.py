from Employee import enrollment
from Employee import parttime

class Course():
    def __init__(self, ID, title, internatioonal, EmploymentofDate):
        self.ID = ID
        self.title = title
        self.internatioonal = internatioonal
        self.EmploymentofDate = EmploymentofDate

    def course1(self):
        print(self.ID)
        print(self.title)
        print(self.internatioonal)
        print(self.EmploymentofDate)


class Enrollment1(enrollment):
    pass


class PartTime1(parttime):
    pass