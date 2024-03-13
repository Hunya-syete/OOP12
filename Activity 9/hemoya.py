class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hours_worked = 0

    def display_employee(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

    def give_raise(self, amount):
        self.salary += amount
        return f"Employee {self.name}'s new salary after raise is: {self.salary}"

    def log_hours(self, hours):
        self.hours_worked += hours
        return f"Employee {self.name} has now worked {self.hours_worked} hours."


# Creating an instance of the Employee class
employee1 = Employee(1, "Jaysever Hemoya", "computer Engineer", 50000)

# Displaying the employee
print(employee1.display_employee())

# Giving the employee a raise
print(employee1.give_raise(5000))

# Logging hours worked by the employee
print(employee1.log_hours(8))
