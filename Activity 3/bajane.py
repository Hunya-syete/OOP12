Action_recommendation = "john wick"
comedy_recommendation = "good boys"
thriller_recommendation = "herro"
general_recommendations = "alive"

list_of_genre = ["Comedy, thriller action"]

genre = input(f"[What movie  do you prefer?]- {list_of_genre}:")
rating = int(input(" [rate 1-10]- "))

if genre == "Action" and rating > 8:
    print(f"watch Action Movie: {Action_recommendation}")
if genre == "Comedy" or rating > 7:
    print(f"watch Comedy Movie: {comedy_recommendation}")
elif genre != "thriller" and rating < 6:
    print(f" thriller Movie: {thriller_recommendation} ")
if genre not in list_of_genre:
    print(f" Recommend the movie to watch is: {general_recommendations}")
