class employee:
    def __init__(self,title,Id,dateOfEmployment):
        self.title = title
        self.Id = Id
        self.dateOfEmployment = dateOfEmployment

    def displayEmployee(self):
        print("Id:",self.Id,"\nTitle:",self.title,"\nDateOfEmployment:",self.dateOfEmployment)

E1 = employee("Senior Computer Engineer","125982","2019-05-25")
E2 = employee("Junior Computer Engineer","125662","2022-02-11")



