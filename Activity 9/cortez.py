class employee:
      def __init__(self, name, email, phone_no):
            self.name = name
            self.email = email
            self.phone_no = phone_no

emp1 = employee("Courage Dog", "couragecowardly@gmail.com", "09706157078")
emp2 = employee("Steven Universe", "stevenuniverse@gmail.com", "09300217525")

print(f"Name:{emp1.name} \nEmail:{emp1.email} \nPhone:{emp1.phone_no}")
print()
print(f"Name:{emp2.name} \nEmail:{emp2.email} \nPhone:{emp2.phone_no}")
