class Dog:
    def __init__(self, size: object, color: object, breed: object) -> object:
        self.size = size
        self.color = color
        self.breed = breed

    def bark(self):
        return "Woof!"

    def display_dog(self):
        return f"This is a {self.size} {self.color} {self.breed}."

# Creating instances of the Dog class
chihuahua = Dog("big", "brown", "Chihuahua")
bulldog1 = Dog("big", "brown", "Bulldog")
bulldog2 = Dog("medium-sized", "white", "Bulldog")
bisaya = Dog("small", "Variegated", "philippine dog")

# Displaying the dogs
print(chihuahua.display_dog())
print(bulldog1.display_dog())
print(bulldog2.display_dog())
print(bisaya.display_dog())

# SampleText
SampleText1 = "isyu:- basta gihiktan ayawg hikapa kay mama-ak"
print(SampleText1)
