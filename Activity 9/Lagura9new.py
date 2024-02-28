class Employee:
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile


    def print_employee_details(self):
        print("\nName: ", self.name)
        print("email: ", self.email)
        print("mobile: ", self.mobile)

# Instantiate the Employee class two times with different information
employee1 = Employee("jerry", "jerry@gmail.com", "0989898890")
employee2 = Employee("mie", "mie@gmail.com", "09123423549")

# Display all the properties of the object
print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
