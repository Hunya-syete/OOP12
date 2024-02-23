class Employee():
    def __init__(self, Name, Email, MobileNo):
        self.Name = Name
        self.Email = Email
        self.MobileNo = MobileNo

Marmar = Employee(Name="Marmar", Email="Marmar@Bicbic.ph", MobileNo="0999-987-789")
Marbe = Employee(Name="Marbe", Email="Marbe@Bicbic.ph", MobileNo="0999-654-456")

print("Here are the current employees for this company with their basic INFORMATION.")
print("")
print("Employee 1:")
print("Employee Name: " + Marmar.Name)
print("Employee Email: " + Marmar.Email)
print("Employee Mobile No: " + Marmar.MobileNo)

print("")
print("Employee 2:")
print("Employee Name: " + Marbe.Name)
print("Employee Email: " + Marbe.Email)
print("Employee Mobile No: " + Marbe.MobileNo)