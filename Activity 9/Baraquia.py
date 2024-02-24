class Employee:
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile

# Instantiate the Employee class
employee1 = Employee("John Doe", "john.doe@example.com", "1234567890")
employee2 = Employee("Jane Smith", "jane.smith@example.com", "9876543210")
employee3 = Employee("Mike Johnson", "mike.johnson@example.com", "4567890123")

# Display properties of each employee
print("Employee 1:")
print("Name:", employee1.name)
print("Email:", employee1.email)
print("Mobile:", employee1.mobile)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("Email:", employee2.email)
print("Mobile:", employee2.mobile)

print("\nEmployee 3:")
print("Name:", employee3.name)
print("Email:", employee3.email)
print("Mobile:", employee3.mobile)
