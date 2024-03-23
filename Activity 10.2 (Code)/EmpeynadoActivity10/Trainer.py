class trainer:
    def __init__(self,id,domain,salary,courses,salaryRaise):
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = courses
        self.salaryRaise = salaryRaise

    def got_raise(self):
        print("New Salary: ", (self.salary + self.salaryRaise))

    def displayTrainer(self):
        print("Id: ", self.id, "\nDomain: ", self.domain, "\nSalary: ", self.salary, "\nCourses: ",self.courses)

T1 = trainer("256489", "Programming",10000, "OOP \nPLD", 1000)
T2 = trainer("256897", "Science",10000, "Physics \nChemistry", 0)


