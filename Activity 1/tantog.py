x = "10"
y = "10"
print(int(x) + int(y))

name = inout("Enter Full Name: ")
email = input("Enter Email: ")
print("Name: " + name)
print("Email: " + email)

# string
name = "Ian"
food = "Hotdog"
game = "console"

sampleText1 = "My name {}  i llove {} and playing {}"
sampletext1a = sampletext1.format(name, food, game)
print(sampleText1a)

sampleText2 = "My name is {0} i love {1} and playing {2}"
sampleText2a = sampletext2.formet(name, food, game)
print(sampleText2a)

sampleText3 = "My name is {newname} i love {newfood} and playing {newgame}"
sampleText3a = sampletext3.format(newname="ian", newfood="spaghetti", newgame="volleyball")
print(sampleText3a)

item = "chocolate"
cost = 35.56511534

sampleText4 = "The product %s cost %.if" % (item, cost)
print(sampleText4)

inport = math
grade1 = 95.68
grade2 = 94.45

print(round(grade1,1))
print(math.ceil(grade1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade2))
print(poe(2,3))
print(2**3)
