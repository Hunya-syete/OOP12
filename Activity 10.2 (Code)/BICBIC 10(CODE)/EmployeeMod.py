class Employee:
    def __init__(self, id, title, date_of_employment, international):
        self.id = id
        self.title = title
        self.international = international
        self.date_Of_employment = date_of_employment

    def P_Employee(self):
        print("\n", self.id, "\n", self.title, "\n", self.date_Of_employment, "\n", self.international)

class Enrollment:
    def __init__(self):
        self.enrolled = []

    def a_enroll(self, enroll):
        self.enrolled.append(enroll)

    def P_Enrollment(self):
        for enroll in self.enrolled:
            print("",enroll,end=",")

class PartTime:
    def __init__(self, is_part_time=False):
        self.is_part_time = bool(is_part_time)

    def P_PartTime(self):
        if self.is_part_time:
            print("\n",f'-', "Is working Part Time.")
        else:
            print("\n",f'-', "Is not working Part Time.")

class Probation:
    def __init__(self, is_on_probation=True):
        self.is_on_probation = bool(is_on_probation)

    def P_Probation(self):
        if self.is_on_probation:
            print("", f'-', "Is on Probation.")
        else:
            print("", f'-',"Is not on Probation")