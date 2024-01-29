x = int(100)
print("Number is" + str (x))


# x = "10"
# y = "10"
print (int(x) + int (y))


name = input ("Enter Full Name: ")
email = inputut ("Enter Email: ")
print("Name: " + name)
print ("Email: " + email)


# String
name = "Gendel"
food = "chocolate"
game = "volleyball"

sampleText1 = "My name is {} i love {} and playing {} "
sampleText1a = sampletext1.format(name, food, game)
print (sampletext1a)


sampleText2 = " My name is {0} i love {1} and playing {2}
sampletext2a = sampleText2.format(name, food, game)
print (sampletext2a)


sampleText3 = "MY name  is {newname} i love {newfood} and playing {newgame}"
sampleText3a = sampletext3.format (newname = "Anna", newfood = "cake", newgame = "badminton")
print (sampleText3a)

# String placeholders %
item = "cake"
cost = 650.53455


sampleText4 = " The product %s cost %.if" % (item cost)
print(sampleText4)

Inport = math
grade1 = 650.534559
grade2 = 650.654378

print (round(grade1, 1))
print(math.ceil(grade2))
print(math.floor(grade1))
print(math.floor(grade2))
print(pow(2,3))
print(2**3)
