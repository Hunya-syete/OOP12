print("\nActivity 8")

print("\n=========")
print("Dog Class")
print("=========")


class Dog():
    def __init__(self, name, color, breed, size):
        self.name = name
        self.color = color
        self.breed = breed
        self.size = size

    def Dog1(self):
        print("\nDog 1")
        print(self.name)
        print(self.color)
        print(self.breed)
        print(self.size)

    def Dog2(self):
        print("\nDog2")
        print(self.name)
        print(self.color)
        print(self.breed)
        print(self.size)

    def Dog3(self):
        print("\nDog3")
        print(self.name)
        print(self.color)
        print(self.breed)
        print(self.size)


Dog1 = Dog("Dash", "Gold", "Golden Retriever", "Large Size")
Dog2 = Dog("Tim", "White", "Husky", "Large Size")
Dog3 = Dog("Charlie", "Brown", "Chihuahua", "Small Size")

Dog1.Dog1()
Dog2.Dog2()
Dog3.Dog3()
