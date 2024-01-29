x = int(100)
print("Number is " + str(x))

x = "10"
y = "10"
print(int(x) + int(y))

name =  input("Enter Full Name: ")
email = input("Enter Email: ")
print("Name: " + name)
print("Email: " + email)

#String Place holder {}
name = "John"
food = "Lechon"
game = "Pc"

sampleText1 = "My name is {} I love {} and playing {}"
sampleText1a = sampleText1.format(name, food, game)
print(sampleText1a)

sampleText2 = "My name is {0} I love {1} and playing {2}"
sampleText2a = sampleText2.format(name, food, game)
print(sampleText2a)

sampleText3 = "My name is {newname} I love {newfood} and playing {newgame}"
sampleText3a = sampleText3.format(newname="Joebelle", newfood= "paksiw", newgame="Dampa")
print(sampleText3a)

#String placeholders %
item = "shabuhayko"
cost = 450.57

sampleText4 = "The product %s cost %.1f" % (item, cost)
print(sampleText4)

import math
grade1 = 95.6534567
grade2 = 95.89734892

print(round(grade1,1))
print(math.ceil(grade1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade2))
print(pow(2,3))
print(2**3)
