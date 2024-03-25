class Person:
    def __init__(self, FName, LName, age, MNumber):
        self.FName = FName
        self.LName = LName
        self.age = age
        self.MNumber = MNumber
        self.address = ()

    def P_Person(self):
        print(f"FirstName: {self.FName}\nLastName: {self.LName}\nAge: {self.age}\nPhoneNumber: {self.MNumber}")

P1 = Person("John", "Karlos", 19, "09012345671")
P1.P_Person()