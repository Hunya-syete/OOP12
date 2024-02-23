class Employee:
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile

lbj = Employee(name="Lebron James", email="lebronjames19@gmail.com", mobile="09068184444")
ad = Employee(name="Anthony Davis", email="davisanthony29@gmail.com", mobile="09671722123")


print(f"Name: {lbj.name}")
print(f"Email: {lbj.email}")
print(f"Mobile Number: {lbj.mobile}")
print("")
print(f"Name: {ad.name}")
print(f"Email: {ad.email}")
print(f"Mobile Number: {ad.mobile}")
