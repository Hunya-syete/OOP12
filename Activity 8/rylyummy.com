class Dog:
    'A simple dog model.'

    def __init__(self, color, size, ):
        'Construct color attributes for an instance of Dog'
        self.color = color.title()
        self.size = size

    def breed(self):
        'Simulate breed dog in response to a command.'
        print(self.name + " is now getting breed.")

    def size(self):
        'Simulate a size in response to a command.'
        print(self.name + " rolled over!")

my_dog = Dog(color='Golden Retriever', size=5)

print("My dog's breed is " + my_dog.color + ".")
print("My dog is " + str(my_dog.size) + " inches .")
