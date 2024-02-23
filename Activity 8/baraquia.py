class Dog:
    def __(self,color,breed,size):
        self.color = color 
        self.breed = breed
        self.size = size
        
        
# Instantiate the Dog class 3 times
dogs = [Dog("White", "Labrador", "Large"), Dog("Brown", "Bulldog", "Medium"), Dog("White", "Poodle", "Small")]
# Display all properties
for dog in dogs:
    print(f"Color: {dog.color}, Breed: {dog.breed}, Size: {dog.size}")
# Modify properties
dogs[0].color = "Grey"
dogs[1].breed = "Beagle"
dogs[2].size = "Medium"
# Display all properties after modification
for dog in dogs:
    print(f"Color: {dog.color}, Breed: {dog.breed}, Size: {dog.size}")
