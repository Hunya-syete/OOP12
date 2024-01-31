# x = int(100)
# print("Number is" + str(x))


#Number1 = "10"
#Number2 = "10"
#print (int(Number1) + int (Number2))


#name = input("Enter Your Full Name: ")
#email = input("Enter Email:" )
#print ("Name: " + name)
#print ("Email: " + email)

#name = "Anna"
#food = "burger"
#game = "console"

SampleText1 = "My name is {} I love {} and playing {}"
SampleText1a = SampleText1.format(name, food, game)
print(SampleText1a)

SampleText2 = "My name is {0} i love {1} and playing {2}"
SampleText2a = SampleText2.format(name, food, game)
print(SampleText2a)

SampleText3 = "My name is {newname} i love { newfood} and playing {newgame}"
SampleText3a = SampleText3.format(newname="Mike", newfood="Cake", newgame="PSP ")
print(SampleText3a)


#string placeholders %
item = "cake"
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
