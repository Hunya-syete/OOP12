x = int(100)
print("number is " + str(x))

x = "10"
y = "10"
print(int(x) + int(y))

name = input("Enter Full Name: ")
email = input("Enter Email: ")
print("Name: " + name)
print("Email: " + email)

name = "anna"
food = "burger"
game = "console"

sampleText1 = "My name is {} i love {} and playing {}"
sampleText1a = sampleText1.format(name, food, game)
print(sampleText1a)

sampleText2 = "My name is {0} i love {1} and playing {2}"
sampleText2a = sampleText2.format(name, food, game)
print(sampleText2a)

sampleText3 = "My name is {newname} i love {newfood} and playing {newgame}"
sampleText3a = sampleText3.format(newname= "mike", newfood="spaghetti", newgame="volleyball")
print(sampleText3a)

item = "Chocolate"
costs = 35.5651534

sampleText4 = "The product %s costs % if " % (item, costs)
print(sampleText4)

import math
grade1 = 95.68
grade2 = 94.45

print(round(grade1,1))
print(math.ceil(grade1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade2))
print(pow(2, 3))
print(2**3)
