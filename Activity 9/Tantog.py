class employee:
    def __init__(self, name, email, mobile_no):
         self.name = name
         self.email = email
         self.mobile_no = mobile_no

employee1 = employee("Jollibee", "hilawangmanok@gmail.com", "09995409810")
employee2 = employee("Mcdonalds", "walayunligravy@gmail.com", "09831118345")

print(f"Name:{employee1.name} \nEmail:{employee1.email} \nMobile Number:{employee1.mobile_no}")
print()
print(f"Name:{employee2.name} \nEmail:{employee2.email} \nMobile Number:{employee2.mobile_no}")
