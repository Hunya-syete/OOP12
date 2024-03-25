from Address import Address
class Person:
    def __init__(self, first_name: str, last_name: str, age: int, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number

    def add_address(self, address: Address):
        return Address(address.country, address.city, address.street)


# People


Person1 = Person("Mc", "Alexis", 30, "09698271312")
Person1.add_address = Address("Philippines", "Dipolog", "Gomez")

Person2 = Person("Harold", "Onineza", 30, "09875642389")
Person2.add_address = Address("Philippines", "Dipolog", "Herrera")

# Person1 info
Mcinfo = (f"name:{Person1.first_name} {Person1.last_name}\n"
          f"age:{Person1.age}\n"
          f"phone number:{Person1.phone_number}\n"
          f"address:{Person1.add_address.country}, {Person1.add_address.city} City, {Person1.add_address.street} st.")
print()
# Person2 info
Harold = (f"name:{Person2.first_name} {Person2.last_name}\n"
          f"age:{Person2.age}\n"
          f"phone number:{Person2.phone_number}\n"
          f"address:{Person2.add_address.country}, {Person2.add_address.city} City, {Person2.add_address.street} st.")


class Employee(Person):
    def __init__(self, name, age, phone_number):
        super().__init__(name, age, phone_number)
        
    def mc(self):
        return Mcinfo


Mc = Employee.mc
print(Mc)

class Trainer(Person):
    pass