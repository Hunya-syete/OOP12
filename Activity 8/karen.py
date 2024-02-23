class Dog():
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

dog1 = Dog(name="Max", age="2", breed="Askal", color="Brown")
dog2 = Dog(name="Ryl", age="2", breed="Poodle", color="White")

print(dog1.name)
print(dog1.age)
print(dog1.breed)
print(dog1.color)

print(dog2.name)
print(dog2.age)
print(dog2.breed)
print(dog2.color)
