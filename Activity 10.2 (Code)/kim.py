class Address:
    def __init__(self, country, city, street, postal):
        self.country = country
        self.city = city
        self.street = street
        self.postal = postal


class Person:
    def __init__(self, first_name, last_name, phone_number, title):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.title = title
        self.address = None


class Employee(Person):
    def __init__(self, first_name, last_name, phone_number, title, id, international, field, date_of_employment):
        super().__init__(first_name, last_name, phone_number, title)
        self.id = id
        self.international = international
        self.field = field
        self.date_of_employment = date_of_employment
        self.enrolled = []


class Trainer(Person):
    def __init__(self, first_name, last_name, phone_number, title, id, domain, salary):
        super().__init__(first_name, last_name, phone_number, title)
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = []


class Enrollment:
    def __init__(self, employee, course, grade, date):
        self.employee = employee
        self.course = course
        self.grade = grade
        self.date = date


# Create instances of Address
address1 = Address("USA", "New York", "123 Main Street", "10001")

# Create instances of Employee and Trainer
employee = Employee("John", "Doe", "1234567890", "Manager", "E001", True, "IT", "2020-01-01")
employee.address = address1
trainer = Trainer("Jane", "Doe", "0987654321", "Engineer", "T001", "IT", 50000)
trainer.address = address1

# Create instances of Enrollment
enrollment1 = Enrollment(employee, "Python Programming", "A", "2022-01-01")
employee.enrolled.append(enrollment1)
