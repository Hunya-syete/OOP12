class Person:
    def __init__(self, first_name, last_name, phone_number, title):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.title = title
        self.addresses = []


class Address:
    def __init__(self, country, city, street, postal):
        self.country = country
        self.city = city
        self.street = street
        self.postal = postal


class Employee(Person):
    def __init__(self, first_name, last_name, phone_number, title, id, international, field, date_of_employment):
        super().__init__(first_name, last_name, phone_number, title)
        self.id = id
        self.international = international
        self.field = field
        self.date_of_employment = date_of_employment
        self.enrolled = []

    def add_enrolled(self, course):
        self.enrolled.append(course)

    def is_part_time(self):
        # logic for checking if part-time
        pass

    def is_on_probation(self):
        # logic for checking if on probation
        pass


class Trainer(Person):
    def __init__(self, first_name, last_name, phone_number, title, id, domain, salary, courses):
        super().__init__(first_name, last_name, phone_number, title)
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = courses

    def got_raise(self):
        # logic for raise
        pass

    def add_course(self, course):
        self.courses.append(course)


class Course:
    def __init__(self, name):
        self.name = name


class Enrollment:
    def __init__(self, employee, course, grade, date):
        self.employee = employee
        self.course = course
        self.grade = grade
        self.date = date

    def set_grade(self, grade):
        self.grade = grade


# Create instances of Address
address1 = Address("Isis", "sto.domingo", "123 Main Street", "10001")
address2 = Address("South", "new lebanon", "456 Broadway", "90001")

# Create instances of Person
person1 = Person("Maverick", "kim", "09700439643", "Engineer")
person1.addresses.append(address1)
person2 = Person("Jackie", "kim", "09817108580", "Engineer")
person2.addresses.append(address2)

# Create instances of Employee and Trainer
employee = Employee("Maverick", "kim", "1234567890", "Manager", "E001", True, "IT", "2020-01-01")
employee.addresses.append(address1)
trainer = Trainer("Jackie","kim", "0987654321", "Engineer", "T001", "IT", 50000, [])
trainer.addresses.append(address2)

# Create instances of Course
course1 = Course("Python Programming")
course2 = Course("Object-Oriented Programming")

# Create instances of Enrollment
enrollment1 = Enrollment(employee, course1, "A", "2022-01-01")
enrollment2 = Enrollment(employee, course2, "B", "2022-02-01")

# Print the details
print(f"Employee {employee.first_name} is enrolled in {len(employee.enrolled)} courses.")
print(f"Trainer {trainer.first_name} is teaching {len(trainer.courses)} courses.")

