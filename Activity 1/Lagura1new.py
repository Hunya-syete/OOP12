x = int(100)
print("Number is" + str(x))


Number1 = "10"
Number2 = "10"
print(int(Number1) + int(Number2))


name = input("Name:")
email = input("Enter Email:")
print("Name: " + name)
print ("Email: " + email)

name = "jerry"
food = "burger"
game = "cards"

SampleText1 = "My name is {} I love {} and playing {}."
SampleText1a = SampleText1.format(name, food, game)
print(SampleText1a)


SampleText2 = "My name is {0} i love {1} and playing {2}."
SampleText2a = SampleText2.format(name, food, game)
print(SampleText2a)


SampleText3 = "My name is {} i love {} and playing {}."
SampleText3a = SampleText3.format( "JC", "jam", "PS5")
print(SampleText3a)


#string placeholders %

item = "jam"
cost = 120

sampletext4 = "The product %s cost %.if" % (item, cost)
print(sampletext4)
