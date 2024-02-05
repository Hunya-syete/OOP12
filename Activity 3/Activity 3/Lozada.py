user = input("Enter Name: ")
print("-------------------------------")
print("Genre Selections")
print(" ")
print("Thriller = 6")
print("Comedy = 7")
print("Action = 8")
print("Others(choose any numbers except 6,7,8):______. ")
print("--------------------------------")
genre = str(input("Enter genre #: "))
print("Chosen Genre #: " + genre)

if genre == "6":
    print("Hello " + user + "! We recommend Thriller Saw 3.")

if genre == "7":
    print("Hello " + user + "! We recommend Comedy hit Praybet Benjamen.")

if genre == "8":
    print("Hello " + user + "! We recommend Action blockbuster Spiderman Homecoming. ")

if genre != "6" and genre != "7" and genre != "8":
    print("Hello " + user + "! We recommend Lord of The Rings.")
