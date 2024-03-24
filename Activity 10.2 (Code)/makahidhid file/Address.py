class Address:
    def __init__(self,country,city,street,zipcode):
        self.country = country
        self.city=city
        self.street = street
        self.zipcode = zipcode

    def printcountry(self):
        print(self.country,self.city,self.street,self.zipcode)