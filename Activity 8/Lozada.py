class Dog():
    def add_dog(self, size, color, breed):
        self.size = size
        self.color = color
        self.breed = breed

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_breed(self):
        return self.breed

    def __str__(self):
        return f'Dog: {self.size, self.color, self.breed}'

dog1 = Dog()
dog1.add_dog('small', 'brown', 'chihuahua')
dog2 = Dog()
dog2.add_dog('big', 'black', 'bulldog')
dog3 = Dog()
dog3.add_dog('medium-sized', 'white', 'poodle')

print('Dog Class')
print(dog1.get_size(), dog1.get_color(), dog1.get_breed())
print(dog2.get_size(), dog2.get_color(), dog2.get_breed())
print(dog3.get_size(), dog3.get_color(), dog3.get_breed())

dog1.size = 'big'
dog2.color = 'brown'
dog3.breed = 'bulldog'
print('')
print('After Modifications:')
print(dog1.get_size(), dog1.get_color(), dog1.get_breed())
print(dog2.get_size(), dog2.get_color(), dog2.get_breed())
print(dog3.get_size(), dog3.get_color(), dog3.get_breed())


