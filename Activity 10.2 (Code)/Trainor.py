from Person1 import Person
class Trainor(Person):
    def __init__(self,name, age, id, title, salary):
        self.name = name
        self.age = age
        self.id = id
        self.title = title
        self.salary = salary

    def P_Trainor(self):
        print(f"Name: {self.name}\nAge: {self.age}\nTitle: {self.title}\nSalary: {self.salary}")

print("\n")
T1 = Trainor("Bill", 30, "123456", "Head", 100000)
T1.P_Trainor()