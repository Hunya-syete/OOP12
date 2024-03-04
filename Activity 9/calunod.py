class employee:
      def __init__(self, name, email, phone_no):
            self.name = name
            self.email = email
            self.cell_no = phone_no
employer1 = employee("Aling Myrna", "alingmyrna@yahoo.com", "09321321342")
employer2 = employee("Karen Calunod", "calunodkaren@yahoo.com", "09123123123")
print(f"Name:{employer1.name} \nEmail:{employer1.email} \nPhone:{employer1.cell_no}")
print()
print(f"Name:{employer2.name} \nEmail:{employer2.email} \nPhone:{employer2.cell_no}")
