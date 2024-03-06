x = int(100)
print("Number is " + str(x))

Number1 = "50"
Number2 = "20"
print(int(Number1) + int(Number2))

Fname = input("Enter First Name: ")
Lname = input("Enter Last Name: ")
email = input("Enter Email: ")
print("First Name: " + Fname)
print("Last Name: " + Lname)
print("Email: " + email)

name = "Jackie"
food = "cake"
game = "mobile legends"

sampleText1 = "My name is {} i love {} and playing {}"
sampleText1a = sampleText1.format(name, food, game)
print(sampleText1a)

sampleText2 = "My name is {2} i love {0} and playing {1}"
sampleText2a = sampleText2.format(name, food, game)
print(sampleText2a)

sampleText3 = "My name is {newfood} i love {newname} and playing {newname}"
sampleText3a = sampleText3.format(newname="Mark", newfood="macaroni", newgame="basketball")
print(sampleText3a)

item = "Dairy milk"
cost = 125.5
sampleText4 = "The product %s costs %.5f" % (item, cost)
print(sampleText4)

import english
grade1 = 89.4
grade2 = 87.555

print(round(grade1,1))
print(english.ceil(grade1))
print(english.ceil(grade2))
print(english.floor(grade1))
print(english.floor(grade2))
print(pow(8,3))
print(2**3)
