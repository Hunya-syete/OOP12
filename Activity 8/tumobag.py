class Dog:
    def __init__(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size

dog1 = Dog(color="Black and White", breed="Boston Terrier", size="Extra small")
dog2 = Dog(color="Brown", breed="Chihuahua", size="Small")
dog3 = Dog(color="Gray", breed="Schnauzer", size="Large")

print("\nDog 1 Details:")
print("Color:", dog1.color)
print("Breed:", dog1.breed)
print("Size:", dog1.size)

print("\nDog 2 Details:")
print("Color:", dog2.color)
print("Breed:", dog2.breed)
print("Size:", dog2.size)

print("\nDog 3 Details:")
print("Color:", dog3.color)
print("Breed:", dog3.breed)
print("Size:", dog3.size)

dog1.color = "Black and Gray"
dog1.size = "Medium"
dog1.breed = "Poodle"

dog2.color = "Golden"
dog2.size = "Large"
dog2.breed = "Golden Retriever"

dog3.color = "White"
dog3.size = "Small"
dog3.breed = "Bulldogs"

print("\nModified Dog 1 Details:")
print("Color:", dog1.color)
print("Breed:", dog1.breed)
print("Size:", dog1.size)

print("\nModified Dog 2 Details:")
print("Color:", dog2.color)
print("Breed:", dog2.breed)
print("Size:", dog2.size)

print("\nModified Dog 3 Details:")
print("Color:", dog3.color)
print("Breed:", dog3.breed)
print("Size:", dog3.size)
