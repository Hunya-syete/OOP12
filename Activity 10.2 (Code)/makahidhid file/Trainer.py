class Trainer:
    def __init__(self,salary,tax,courses,get_raise):
        self.salary = salary
        self.tax = tax
        self.courses =courses
        self.get_raise = get_raise

    def printsalary(self):
        print(self.salary,self.tax,self.courses,self.get_raise)
