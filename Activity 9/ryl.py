class employee:
    def __init__(self, name, email, phone_no):
        self.name = name
        self.email = email
        self.cell_no = phone_no


employer1 = employee("Angel Marmis", "angelmarmis11@gmail.com", "09639295154")
employer2 = employee("Ryl ogoc", "ogocrylryan@gmail.com", "09516529255")
print(f"Name:{employer1.name} \nEmail:{employer1.email} \nPhone:{employer1.cell_no}")
print()
print(f"Name:{employer2.name} \nEmail:{employer2.email} \nPhone:{employer2.cell_no}")
