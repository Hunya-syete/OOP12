class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_properties(self):
        print(f"Name: {self.name}, Email: {self.email}")

# Example usage
person1 = Person("Jhon", "jhonthegreat233@gmail.com")
person1.display_properties()
person2 = Person("ryl", "rylbeautiful33@gmail.com")
person2.display_properties()
