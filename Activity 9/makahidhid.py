class Employee:
    def __init__(self, name, email, mobile_number):
            self.name = name
            self.email = email
            self.mobile_number = mobile_number

# Instantiate Employee class with different information
employee1 = Employee("richard", "makahidhid@gmail.com", "906-866-4066")
employee2 = Employee("Dave", " dave alolod@gmail.com", "987-654-3210")

# Display properties of each object
print("Employee 1:")
print("Name:", employee1.name)
print("Email:", employee1.email)
print("Mobile Number:", employee1.mobile_number)

print("\nEmployee 2:")
print("Name:", employee2.name)
print("Email:", employee2.email)
print("Mobile Number:", employee2.mobile_number)
