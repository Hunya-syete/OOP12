Genre = input("Preferable genre:")
Rating = int(input("rating:"))
Action = "Tekken the Movie"
Funny = "Shazam!"
Horror = "The Quiet Place"
recommendation = "Five Nights At Freddy's, \nThe Justice League, \nFast and Furious X"

list_of_genre = "Action, Comedy or Thriller"

print(f"Genre: {Genre}")
print(f"Rating: {Rating}")


if Genre == "action" and Rating > 8:
        print(f"Recommended Action Movie: {Action}")

if Genre == "comedy" and Rating > 7:
           print(f"Recommended Action Movie: {Funny}")

if Genre == "romance" and Rating < 6:
            print(f"Recommended Action Movie: {Horror}")

if Genre not in list_of_genre:
           print(f"General Recomendation is: \n{recommendation}")
