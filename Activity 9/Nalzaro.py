class Person:
    def __init__(self, name, email, Mobile_Number):
        self.name = name
        self.email = email
        self.Mobile_Number = Mobile_Number

    def display_properties(self):
        print(f"Name: {self.name}, Email: {self.email}, Mobile_Number: {self.Mobile_Number}")

# Example usage
person1 = Person("Renz Nalzaro", "cunahapnalzaro1@gmail.com", "09514345634")
person1.display_properties()
person2 = Person("Rodel", "SiRodel-1234@gmail.com", "09126748934")
person2.display_properties()
person3 = Person ("Mc Alexis Calabria", "example@gmail.com", "09993412875")
person3.display_properties()
