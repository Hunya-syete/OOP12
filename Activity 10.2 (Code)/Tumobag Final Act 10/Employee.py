from Person1 import Person
class Employee(Person):
    def __init__(self, name, id, title, salary):
        self.name = name
        self.id = id
        self.title = title
        self.salary = salary

    def P_Employee(self):
        print(f"Name: {self.name}\nId: {self.id}\nTitle: {self.title}\nSalary: PHP {self.salary}")

print("\n")
E1 = Employee("Angelo", 123, "CEO", 50000)
E1.P_Employee()
