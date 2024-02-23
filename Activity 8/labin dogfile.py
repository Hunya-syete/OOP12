class Dog:
    def __init__(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size

    def display_properties(self):
        print(f"Color: {self.color}, Breed: {self.breed}, Size: {self.size}")

# dogs
dog1 = Dog(color="Brown", breed="Labrador", size="Large")
dog2 = Dog(color="Black", breed="Bulldog", size="Medium")
dog3 = Dog(color="White", breed="Hatdog Dog", size="Small")

# properties
print("Properties of Dog 1:")
dog1.display_properties()

print("\nProperties of Dog 2:")
dog2.display_properties()

print("\nProperties of Dog 3:")
dog3.display_properties()

# Modify of dog
dog1.color = "Golden"
dog1.size = "Medium"

print("\nModified Properties of Dog 1:")
dog1.display_properties()

print("Change the number above to modify properties of Dog any dog:")
