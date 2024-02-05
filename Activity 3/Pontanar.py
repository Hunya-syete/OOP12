Movie_Genre = input("What genre?:")
Movie_Rating = int(input("Rating of the Movie?:"))
Actionmovie = "Mission: Impossible - Ghost Protocol (2011)"
Funnymovie = "The Hangover (2009)"
Horrormovie = "Creepin' Creatures"
recommendations = "zombieland, day shift, lisa frankenstien"
Diff_genre = "Action, Comedy or Thriller"

print(f"Genre: {Movie_Genre}")
print(f"Rating: {Movie_Rating}")


if movie == "action" and Rating > 8:
        print(f"Recommended Action Movie: {Actionmovie}")

if movie == "comedy" and Rating > 7:
        print(f"Recommended Action Movie: {Funny}")

if movie == "romance" and Rating < 6:
    print(f"Recommended Action Movie: {Horror}")
else:
    print(f"General Recomendation is: \n{recommendations}")
