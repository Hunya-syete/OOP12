class Person:
    def __init__(self, firstName, lastName, phoneNumber, title):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.title = title
        self.addresses = []

    def addAddress(self, address):
        self.addresses.append(address)

    def printPersonInfo(self):
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Title: {self.title}")
        print("Addresses:")
        for address in self.addresses:
            print(f"- {address.street}, {address.city}, {address.country} {address.postal}")