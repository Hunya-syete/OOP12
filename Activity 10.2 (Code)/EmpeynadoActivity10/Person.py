class person:
    def __init__(self,fName,lName,phoneNum,title,dateOfBirth):
        self.firstName = fName
        self.lastName = lName
        self.phoneNumber = phoneNum
        self.title = title
        self.dateOfBirth = dateOfBirth

    def printPerson(self):
        print("First Name: ",self.firstName, "\nLast Name: ",self.lastName, "\nPhone Number: ",self.phoneNumber, "\nTitle: ",self.title, "\nDate of Birth: ",self.dateOfBirth)

    def displayPerson(self):
        print("First Name: ",self.firstName, "\nLast Name: ",self.lastName,"\nPhone Number: ",self.phoneNumber)

P1 = person("John","Cortez","09227845969","Student","1999-12-12")
P2 = person("Jade","Bicbic","09236578956","Student","1998-02-14")
P3 = person("Karen", "Bajane","09784512662","Senior Computer Engineer","1999-12-25")
P4 = person("Luie", "Alolod", "09162547879","Junior Computer Engineer","1995-05-16")
P5 = person("Vincel","Padilla","09165794512","Trainer","1999-05-14")
P6 = person("Mark", "Reyes", "090845158742","Trainer","1999-01-25")

