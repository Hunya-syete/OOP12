action_recommendation = "Rebel Moon"
comedy_recommendation = "Trolls"
thriller_recommendation = "Five Nights at Freddy's"
general_recommendations = "Poor Things"

list_of_genre = "Action, Comedy or Romance"

genre = input(f"What movie genre do you prefer? {list_of_genre}:")
rating = int(input("At what rating? "))

if genre == "Action" and rating > 10:
    print(f"Recommended Action Movie: {action_recommendation}")

if genre == "Comedy" or rating > 8:
    print(f"Recommended Comedy Movie: {comedy_recommendation}")

elif genre != "Romance" and rating < 5:
    print(f"Recommended Thriller Movie: {thriller_recommendation} ")

if genre not in list_of_genre:
    print(f"General Recommendation is: {general_recommendations}")
