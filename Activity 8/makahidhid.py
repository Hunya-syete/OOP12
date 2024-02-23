class Dog:
    def __init__(self, breed, size):
        self.breed = breed
        self.size = size

# Instantiate the Dog class 3 times
dog1 = Dog(breed="Labrador", size="Large")
dog2 = Dog(breed="Poodle", size="Small")
dog3 = Dog(breed="German Shepherd", size="Medium")

# Display properties of the instantiated dogs
print("Dog 1 - Breed:", dog1.breed, "Size:", dog1.size)
print("Dog 2 - Breed:", dog2.breed, "Size:", dog2.size)
print("Dog 3 - Breed:", dog3.breed, "Size:", dog3.size)

# Modify the properties of the dogs
dog1.size = "Medium"
dog2.breed = "Golden Retriever"

# Display modified properties
print("\nAfter Modification:")
print("Dog 1 - Breed:", dog1.breed, "Size:", dog1.size)
print("Dog 2 - Breed:", dog2.breed, "Size:", dog2.size)
print("Dog 3 - Breed:", dog3.breed, "Size:", dog3.size)
