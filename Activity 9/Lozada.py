class Employee:
    def __init__(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

employee1 = Employee("Joebelle", "Joebelle@gmail.com", "09557788991")

employee2 = Employee("john", "john@gmail.com", "09887766552")

print("Employee")
print('Name: ', employee1.name)
print('Email: ', employee1.email)
print('Mobile number: ', employee1.mobile_number)
print("")
print('Name: ', employee2.name)
print('Email: ', employee2.email)
print('Mobile number: ', employee2.mobile_number)
