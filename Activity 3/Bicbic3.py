print("Please pick from the available genres")
print("Genres: Action, Comedy, Thriller, Romance,")
MoviePref = str(input("Genre: "))

ValidGenres = {"Action", "Comedy", "Thriller", "Romance"}

while True:
    if MoviePref not in ValidGenres:
        print("Please input a valid genre.")
        MoviePref = str(input("Pick from the the available genres: "))
    break

print("Give a rating of a movie you want to watch from 1 to 10.")
Rating = int(input("Rating: "))

while True:
    if Rating > 10 or Rating < 1:
        print("Give a rating between (1-10)")
        Rating = int(input("(1-10): "))
    break

if MoviePref == "Action" and Rating >= 9:
    print("I can suggest: Mission:Impossible")

if MoviePref == "Comedy" or Rating == 8:
    print("I can suggest: 22 Jump street")

if MoviePref == "Action" and Rating <= 5 or MoviePref == "Comedy" and Rating <= 5 or MoviePref == "Thriller" and Rating <= 5:
    print("I can suggest: Scream")

if MoviePref == "Action" and Rating <= 7 or "Comedy" and Rating <= 7 or "Thriller" and Rating <= 7 or "Romance" and Rating <= 7:
    print("I can suggest: Princess Swap")
if MoviePref == "Romance" and Rating <= 5:
    print("I can suggest: Princess Swap")
