class Dog:
    def __init__(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size

# Instantiate the Dog class
dog1 = Dog("Brown", "Labrador Retriever", "Large")
dog2 = Dog("White", "Poodle", "Medium")
dog3 = Dog("Black", "German Shepherd", "Large")

# Display properties of each dog
print("Dog 1:")
print("Color:", dog1.color)
print("Breed:", dog1.breed)
print("Size:", dog1.size)

print("\nDog 2:")
print("Color:", dog2.color)
print("Breed:", dog2.breed)
print("Size:", dog2.size)

print("\nDog 3:")
print("Color:", dog3.color)
print("Breed:", dog3.breed)
print("Size:", dog3.size)

# Modify the properties of a dog
dog1.color = "Red"
dog2.breed = "Golden Retriever"
dog3.size = "Medium"

# Display modified properties
print("\nModified Dog 1:")
print("Color:", dog1.color)
print("Breed:", dog1.breed)
print("Size:", dog1.size)

print("\nModified Dog 2:")
print("Color:", dog2.color)
print("Breed:", dog2.breed)
print("Size:", dog2.size)

print("\nModified Dog 3:")
print("Color:", dog3.color)
print("Breed:", dog3.breed)
print("Size:", dog3.size)
