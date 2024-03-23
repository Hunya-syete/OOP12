class address:
    def __init__(self,country,city,street,postal):
        self.country = country
        self.city = city
        self.street = street
        self.postal = postal

    def printAdd(self):
        print("Country: ", self.country, "\nCity: ", self.city, "\nStreet: ", self.street, "\nPostal: ", self.postal)

Add1 = address("France","Dunkerque","57 rue Cazade","59140")
Add2 = address("Canada","Brantford","2543 Lyons Avenue","N3R 7J2")
Add3 = address("Philippines","Dipolog City","Gonzales","7100")
Add4 = address("Philippines","Dipolog City","Mabinay","7100")
Add5 = address("France","Dunkerque","85 rue Cazade","59140")
Add6 = address("Canada","Brantford","6897 Lyons Avenue","N3R 7J2")