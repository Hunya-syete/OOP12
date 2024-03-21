class Trainer:
    def __init__(self, ID, domain, salary=0):
        self.ID = ID
        self.domain = domain
        self.salary = salary
        self.address = ()



    def train(self):
        print(self.ID)
        print(self.domain)
        print(self.salary)

class Raise:
    def __init__(self, got_raise=False):
        self.got_raise = bool(got_raise)

    def Raise(self):

         if self.got_raise:
            print("\nHas a Raise.")

         else:
            print("\nNot have a Raise")





