class Dog:
    def __(self, color, breed, size):
# Instantiate the Dog class 3 times
dogs = [Dog("Black", "Belgian Sheperd", "Medium"), Dog("White and black", "Dalmatians", "Large"), Dog("White", "German Shepherd", "Small")]
# Display all properties8
for dog in dogs:
    print(f"Color: {dog.color}, Breed: {dog.breed}, Size: {dog.size}")
# Modify the properties
dogs[1].color = "Grey"
dogs[2].breed = "Beagle"
dogs[3].size = "Medium"
