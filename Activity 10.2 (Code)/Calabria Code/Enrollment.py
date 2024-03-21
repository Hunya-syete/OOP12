class Enrollment:
    def __init__(self, firstname, lastname, field):
        self.firstname = firstname
        self.lastname = lastname
        self.field = field

    def enrollment1(self):
        print(self.firstname)
        print(self.lastname)
        print(self.field)