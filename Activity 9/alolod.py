class employee:
    def __init__(self, name, email, mobile_no):
         self.name = name
         self.email = email
         self.mobile_no = mobile_no

employee1 = employee("Shanti Dope", "dopedollars@gmail.com", "0987678686")
employee2 = employee("Mc Gregor", "breakaleg@yahoo.com", "0912763872")

print(f"Name:{employee1.name} \nEmail:{employee1.email} \nMobile Number:{employee1.mobile_no}")
print()
print(f"Name:{employee2.name} \nEmail:{employee2.email} \nMobile Number:{employee2.mobile_no}")
