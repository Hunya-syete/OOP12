class Employee():
    def __init__(self, id, title,list_enrolled, date_of_employment):
        self.id = id
        self.title = title
        self.date_of_employment = date_of_employment
        self.list_enrolled = list_enrolled


    def printid(self):
        print(self.id, self.title, self.date_of_employment, self.list_enrolled)
