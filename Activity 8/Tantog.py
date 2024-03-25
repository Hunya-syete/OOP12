class Dog:
    def __init__(self, breed, size, color):
        self.color = color
        self.breed = breed
        self.size = size

# Instantiate the Dog class 3 times
dog1 = Dog(breed="Rottweiller", size="Large", color="Black")
dog2 = Dog(breed="Philippine Forest Dog", size="Medium", color="Brown")
dog3 = Dog(breed="Shih Tzu", size="Small", color="White")

# Display properties of the instantiated dogs
print("Dog 1 - Breed:", dog1.breed, "Size:", dog1.size, "Color:", dog1.color)
print("Dog 2 - Breed:", dog2.breed, "Size:", dog2.size, "Color:", dog2.color)
print("Dog 3 - Breed:", dog3.breed, "Size:", dog3.size, "Color:", dog3.color)

# Modify the properties of the dogs
dog1.size = "Large"
dog2.breed = "Caucasian Shepherd Dog"
dog3.color = "Gray"

# Display modified properties
print("\nAfter Modification:")
print("Dog 1 - Breed:", dog1.breed, "Size:", dog1.size, "Color:", dog1.color)
print("Dog 2 - Breed:", dog2.breed, "Size:", dog2.size, "Color:", dog2.color)
print("Dog 3 - Breed:", dog3.breed, "Size:", dog3.size, "Color:", dog3.color)
