class Dog:

    def _init_(self, color, breed, size):
        self.color = color
        self.breed = breed
        self.size = size

    Dog1 = ("black", "labrador", "medium")
    Dog2 = ("white", "german shepherd", "large")
    Dog3 = ("brown", "french bulldog", "small")


print(f'dog1.color: [black] | breed: [labrador]  |size: [medium]')
print(f'dog2.color: [white] | breed: [german shepherd]  |size: [large]')
print(f'dog3.color: [brown] | breed: [french bulldog]  |size: [small]')
