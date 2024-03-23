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
            print(enroll)

class parttime:
    def __init__(self, isPartTime):
        self.isPartTime = bool(isPartTime)

    def parttime1(self):
        if self.isPartTime:

            self.isPartTime = False
            print("\n- not working Part Time.")

        else:

            self.isPartTime = True
            print("\n- working Part time.")



