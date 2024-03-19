class Trainer:
    def __init__(self, id, domain, bldg_number, salary=0):
        self.id = id
        self.domain = domain
        self.salary = float(salary)
        self.bldg_number = bldg_number

    def P_Trainer(self):
        print("\n", self.id, "\n", self.domain, "\n", self.salary, "\n", self.bldg_number)

class Courses:
    def __init__(self):
        self.courses = []

    def a_course(self, course):
        self.courses.append(course)

    def P_Courses(self):
        for course in self.courses:
            print("",course,end=",")

class Raise:
    def __init__(self, got_raise=False):
        self.got_raise = bool(got_raise)

    def P_Raise(self):
        if self.got_raise:
            print("\n", f'-', "Has a Raise.")
        else:
            print("\n", f'-', "Does not have a Raise")