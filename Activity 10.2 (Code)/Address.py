class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def P_Address(self):
        print(f"Street: {self.street}\nCity: {self.city}\nZip: {self.zip_code}")
print("\n")
A1 = Address("Rizal Street", "Dipolog", zip_code = 7100)
A1.P_Address()