action_recommendation = "Mission Impossible"
comedy_recommendation = "Sometimes Always Never"
thriller_recommendation = "Sound of freedom"
general_recommendations = "It's A Wonderful Life (1946)"

list_of_genre = "Action, Comedy or Romance"

genre = input(f"What movie genre do you prefer? {list_of_genre}:")
rating = int(input("At what rating? "))

if genre == "Action" and rating > 8:
    print(f"Recommended Action Movie: {action_recommendation}")

if genre == "Comedy" or rating > 7:
    print(f"Recommended Comedy Movie: {comedy_recommendation}")

elif genre != "Romance" and rating < 6:
    print(f"Recommended Thriller Movie: {thriller_recommendation} ")

if genre not in list_of_genre:
    print(f"General Recommendation is: {general_recommendations}")
