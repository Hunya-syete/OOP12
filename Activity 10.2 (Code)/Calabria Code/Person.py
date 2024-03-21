
class Person():
        def __init__(self, firstname, lastname, phoneNumber, title):
            self.firstname = firstname
            self.lastname = lastname
            self.phoneNumber = phoneNumber
            self.title = title
            self.address = ()

        def fullname(self):
            print(self.firstname)
            print(self.lastname)
            print(self.phoneNumber)
            print(self.title)


