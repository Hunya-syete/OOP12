class Employee():
    def __init__(self, ID, title, international, dateofemployment):
        self.ID = ID
        self.title = title
        self.international = international
        self.dateofemployment = dateofemployment

    def information(self):
        print(self.ID)
        print(self.title)
        print(self.international)
        print(self.dateofemployment)

class enrollment:
    def __init__(self):
        self.enrolled = []

    def enroll1(self, enroll):
        self.enrolled.append(enroll)

    def Enrollment2(self):
        for enroll in self.enrolled:
            print("\n", enroll)

class parttime:
    def __init__(self, isPartTime=False):
        self.isPartTime = bool(isPartTime)

    def PartTime1(self):
        if self.isPartTime:
            print("\n",f'-', "working Part Time.")
        else:
            print("\n",f'-', "not working Part Time.")


class probation:
    def __init__(self, isOnProbation=True):
        self.isOnProbation = bool(isOnProbation)

    def Probation1(self):
        if self.isOnProbation:
            print("", f'-', "on Probation.")
        else:
            print("", f'-',"not on Probation")