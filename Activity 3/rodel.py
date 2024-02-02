movie = input("Preferable genre:")
Rating = int(input("rating:"))
Actionmovie = "parker"
Funnymovie = "home alone"
Horrormovie = "the nun"
recommendations = "zombieland, day shift, lisa frankenstien"
genre = "Action, Comedy or Thriller"

print(f"Genre: {movie}")
print(f"Rating: {Rating}")


if movie == "action" and Rating > 8:
        print(f"Recommended Action Movie: {Actionmovie}")

if movie == "comedy" and Rating > 7:
        print(f"Recommended Action Movie: {Funny}")

if movie == "romance" and Rating < 6:
    print(f"Recommended Action Movie: {Horror}")
else:
    print(f"General Recomendation is: \n{recommendations}")
