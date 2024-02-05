
Genre = input("kinds of movies:")
Rating = float(input("rating:"))
Action =  "ANNA"
Comedy = "Luck"
Romance = "Araro"
Horror = "Wrong turn"

Movies = "Comedy, Romance, Action, Horror,"

print(f"movies: {Genre}")
print(f"rating: {Rating}")

if Genre == "Action" and Rating > 8:
    print(f"recommended action movie: {Action}")
if Genre == "Comedy" or Rating > 7:
    print(f"recommended comedy movie: {Comedy}")
if Genre == "Romance" and Rating >6:
    print(f"recommended rating movie: {Romance}")
if Genre not in Movies:
    print(f"recommended movie: {Movies}")
