class Employee:
    def __init__(employee, name, email, mobilenumber):
        employee.name = name
        employee.email = email
        employee.mobilenumber = mobilenumber

p1 = Employee("Topper", "topperhotty@gmail.com", 9143556859)
p2 = Employee("Towps", "towperhotty@gmail.com", 99989745187)

print("Name: " + p1.name)
print("Email: " + p1.email)
print("Mobile Number:" + str(p1.mobilenumber))
print("Name: " + p2.name)
print("Email: " + p2.email)
print("Mobile Number:" + str(p2.mobilenumber))
print("Name: " + p1.name +" , " + p2.name)
print("Email: " + p1.email +" , " + p2.email)
print("Mobile Number: " + str(p1.mobilenumber) + " , " + str(p2.mobilenumber))
