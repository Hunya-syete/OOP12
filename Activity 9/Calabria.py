print("\nActivity 9")

print("\n==============")
print("Employee Class")
print("==============")


class Employee():
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile

    def Employee1(self):
        print("\nEmployee 1")
        print(self.name)
        print(self.email)
        print(self.mobile)

    def Employee2(self):
        print("\nEmployee 2")
        print(self.name)
        print(self.email)
        print(self.mobile)


Employee1 = Employee("Mc Alexis D. Calabria", "mcalexis@example.com", "09876566645")
Employee2 = Employee("Dave Alolod", "dave.alolod@example.com", "09651111445")

Employee1.Employee1()
Employee2.Employee2()
