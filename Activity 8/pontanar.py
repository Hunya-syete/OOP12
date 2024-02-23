class Dog():
    def __init__(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size

    def display_properties(self) :
        print (f"Color:(self.color), Breed:(self.breed), Size:(self.size)")
        print ("Dog1:")
        print ("Color:", dog1.color)
        print ("Breed:", dog1.breed)
        print ("Size", dog1. size)

    def main(self):
        dog1 = Dog("Brown", "Poodle", "Medium")
        dog2 = Dog("White", "Chihuahua", "Small")
        dog3 = Dog("Black", "Labrador", "Large")

        #Modifying properties
        dog1. display_properties()
        dog2. display_properties()
        dog3. display_properties()

Browny = Dog("Brown","Poodle", "Medium")
Snowpy = Dog("White","Chihuahua", "Small")
Ramboo = Dog("Black","Labrador", "Large")


print("Dog1:")
print("Color:", Browny.color)
print("Breed:", Browny.breed)
print("Size", Browny.size)

print("Dog2:")
print("Color:", Snowpy.color)
print("Breed", Snowpy.breed)
print("Size",Ramboo.size)

print("Dog3:")
print("Color", Ramboo.color)
print("Breed",Ramboo.breed)
print("Size",Ramboo. size)
