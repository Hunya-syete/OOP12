x = int(100)
print ("number is " + str(x))

x = "10"
y = "10"
print (int(x) + int(y))

name = input("Enter your name: ")
email = input("Enter your Email: ")
print ("name: " + name)
print ("email: " + email)

#String Place Holder {}
name = "John"
food = "Cookie"
game = "PS5"

SampleText1 = "My name is {} I love {} and playing {}"
SampleText1a = SampleText1.format(name, food, game)
print(SampleText1a)

SampleText2 = "My name is {0} i love {1} and playing {2}"
SampleText2a = SampleText2.format(name, food, game)
print(SampleText2a)

SampleText3 = "My name is {newname} i love { newfood} and playing {newgame}"
SampleText3a = SampleText3.format(newname="John", newfood="Cookie", newgame="PS5" )
print(SampleText3a)


#string placeholders %
item = "Cookie"
cost = 450.57

sampletext4 = "The product %s cost %.if" % (item, cost)
print(sampletext4)

import math
grade1 = 95.6534567
grade2 = 95.8973214

print(round(grade1, 1))
print(math.ceil(grade1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade2))
print(pow(2,3))
print(2**3)
