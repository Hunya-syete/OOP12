class Address:
    def __init__(self, country, city, street, bldg_number):
        self.country = country
        self.city = city
        self.street = street
        self.bldg_number = bldg_number

    def P_Adress(self):
        print("\n", self.country, "\n", self.city, "\n", self.street, "\n", self.bldg_number)