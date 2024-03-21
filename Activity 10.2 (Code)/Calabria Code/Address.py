class Address(object):
    def __init__(self, country, city, street, postal_code):
        self.country = country
        self.city = city
        self.street = street
        self.postal_code = postal_code

    def display(self):
        print(self.country)
        print(self.city)
        print(self.street)
        print(self.postal_code)
