Genre = input("Preferable genre:")
rating = int(input("rating:"))
action =("Aliens (1986)")
funny =("8'Three Amigos!  (1986)")
Thriller =("The Sixth Sense (1999) PG-13 | 107 min | Drama, Mystery, Thriller.")
recommendation =("THE BOYS IN THE BOAT (2023) (NEW!) Rating: PG-13, \nSALTBURN (2023) Rating: R., \nOPPENHEIMER (2023) Rating: R.")

list_of_genre = ("Action, Comedy or Thriller")

print(f"Genre: {Genre}")
print(f"Rating: {rating}")


if Genre == "action" and rating > 8:
        print(f"Recommended Action Movie: {action}")

if Genre == "comedy" and rating > 7:
        print(f"Recommended Action Movie: {funny}")

if Genre == "romance" and rating < 6:
        print(f"Recommended Action Movie: {Thriller}")

if Genre not in list_of_genre:
        print(f"General Recomendation is: \n{recommendation}")
