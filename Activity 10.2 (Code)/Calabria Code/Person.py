
from Address import Address
class Person():
        def __init__(self, firstname, lastname, phoneNumber, title):
            self.firstname = firstname
            self.lastname = lastname
            self.phoneNumber = phoneNumber
            self.title = title

        def fullname(self):
            print(self.firstname)
            print(self.lastname)
            print(self.phoneNumber)
            print(self.title)

class address(Address):
        pass

