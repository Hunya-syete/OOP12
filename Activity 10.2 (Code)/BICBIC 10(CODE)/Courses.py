from EmployeeMod import Enrollment
class Course:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code

    def P_Course(self):
        print("\n", self.id, "\n", self.name, "\n", self.code)
class A_Trainer:
    def __init__(self):
        self.trainers = []

    def a_trainer(self, trainer):
        self.trainers.append(trainer)

    def P_C_Trainer(self):
        for trainer in self.trainers:
            print("",trainer,end=",")

class A_Enrollment(Enrollment):
    print("\n")
    pass

class Cancelled:
    def __init__(self, is_cancelled=False):
        self.is_cancelled = bool(is_cancelled)

    def P_Cancelled(self):
        if self.is_cancelled:
            print("\n", f'-', "Is Cancelled")
        else:
            print("\n", f'-', "Is not Cancelled")