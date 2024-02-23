class Employee:
    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number


# Instantiate the Employee class 3 times
employees = [Employee("Maverick kim", "Maverickkim@example.com", "1234567890"),
             Employee("Jane Smith", "janesmith@example.com", "0987654321"),
             Employee("Hanna Son", "Hannason@example.com", "1122334455")]

# Display all properties
for employee in employees:
    print(f"Name: {employee.name}, Email: {employee.email}, Mobile Number: {employee.mobile_number}")
