from Address import Address


class Trainer:
    def __init__(self, ID, domain):
        self.ID = ID
        self.domain = domain


    def train(self):
        print(self.ID)
        print(self.domain)


class Salary:
    def __init__(self, salary):
        self.salary = float(salary)
        if self.salary <= 90:
            print("salary is, ")
        else:
            print("salary is, ")

    def salary(self):
        print(self.salary)


class Got_Raise:
    def __init__(self, got_raise):
        self.got_raise = bool(got_raise)

    def gotraise(self):

        if not self.got_raise:

            self.got_raise = True
            print("\n - Got Raise")

        else:

            self.got_raise = False
            print("\n - Don't have Raise")

class address(Address):
        pass
