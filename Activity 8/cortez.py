class Dog:

    print("Available dogs for adoption.")
    print()

    def set_name(self, name):
        self.name = name
    def set_color(self, color):
        self.color = color

    def set_breed(self, breed):
        self.breed = breed

    def set_size(self, size):
        self.size = size

    def stateMent(self):

            print(f"{self.name}")
            print(f"Color: {self.color}")
            print(f"Breed: {self.breed}")
            print(f"Size: {self.size}")
            print()

dog1 = Dog()
dog1.set_name("Dog 1")
dog1.set_color("Brown")
dog1.set_breed("Akita")
dog1.set_size("Large")

dog2 = Dog()
dog2.set_name("Dog 2")
dog2.set_color("White")
dog2.set_breed("Husky")
dog2.set_size("Medium")

dog3 = Dog()
dog3.set_name("Dog 3")
dog3.set_color("Black")
dog3.set_breed("Terrier")
dog3.set_size("Small")

dog1.stateMent()
dog2.stateMent()
dog3.stateMent()


print("Other modified dogs for adoption.")
print()

def set_name(self, new_name):
    self.name = new_name

def set_color(self, new_color):
    self.color = new_color

def set_breed_color(self,new_breed):
    self.breed = new_breed

def set_size(self, new_size):
    self.size = new_size

    print(f"{self.name}")
    print(f"Color: {self.color}")
    print(f"Breed: {self.breed}")
    print(f"Size: {self.size}")
    print()

mdog1 = Dog()
mdog1.set_name("Dog 1")
mdog1.set_color("White")
mdog1.set_breed("Pomeranian Teacup")
mdog1.set_size("Extra Small")

mdog2 = Dog()
mdog2.set_name("Dog 2")
mdog2.set_color("Brown")
mdog2.set_breed("Bullmastiff")
mdog2.set_size("Extra Large")

mdog3 = Dog()
mdog3.set_name("Dog 3")
mdog3.set_color("Cream")
mdog3.set_breed("Chow-chow")
mdog3.set_size("Medium")

mdog1.stateMent()
mdog2.stateMent()
mdog3.stateMent()
