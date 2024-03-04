class Employee:
    def __init__(self, name, email, mobile_number):
            self.name = name
            self.email = email
            self.mobile_number = mobile_number
# Instantiate Employee class with different information
employee1 = Employee("luie", "luiebajane@gmail.com", "997-304-2881")
employee2 = Employee("jobel", " jumawan@gmail.com", "987-654-3210")
# Display properties of each object
print("Employee 1:")
print("Name:", employee1.name)
print("Email:", employee1.email)
print("Mobile Number:", employee1.mobile_number)
print("\nEmployee 2:")
print("Name:", employee2.name)
print("Email:", employee2.email)


print("Mobile Number:", employee2.mobile_number)
