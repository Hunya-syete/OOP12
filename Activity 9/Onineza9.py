class Person:
    def __init__(self, name, email, Mobile_Number):
        self.name = name
        self.email = email
        self.Mobile_Number = Mobile_Number

    def display_properties(self):
        print(f"Name: {self.name}, Email: {self.email}, Mobile_Number: {self.Mobile_Number}")

# Example usage
person1 = Person("Harold", "oninezah@gmail.com", "09152279543")
person1.display_properties()
person2 = Person("Dave", "davealolod@gmail.com", "09124753572")
person2.display_properties()
person3 = Person ("Renz", "cunahapnalzaro1@gmail.com", "09514345634")
person3.display_properties()
