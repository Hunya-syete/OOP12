class Dog:
    def __init__(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size


    def print_dog_details(self):
        print("\ncolor: ", self.color)
        print("breed: ", self.breed)
        print("size: ", self.size)

# Instantiate the Dog class 3 times with different information
Dog1 = Dog("brown", "german shepherd", "large")
Dog2 = Dog("white", "bulldog", "medium")
Dog3 = Dog("black", "labrador retriever", "small")

# Display all the properties of the object
print("Original Dog Details:")
Dog1.print_dog_details()
Dog2.print_dog_details()
Dog3.print_dog_details()
