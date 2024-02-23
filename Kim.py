class Employee:
    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number  
        
        
# Instantiate the Employee class 3 times
employees = [Employee("John kim", "johnkim@example.com", "09817108580"),
             Employee("Jane Smith", "janesmith@example.com", "09519459335"),
             Employee("Hanna Son", "hannason@example.com", "09639375862")]

# Display all properties
for employee in employees:
    print(f"Name: {employee.name}, Email: {employee.email}, Mobile Number: {employee.mobile_number}")
