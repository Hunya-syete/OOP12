mystery_recommendation = "Enola Hoolmes"
drama_recommendation = "The Hunger Games: The Ballad of Songbirds & Snakes"
thriller_recommendation = "Fast Five"
general_recommendations = "Aquaman"

list_of_genre = "mystery, drama or action "

genre = input(f"What movie genre do you prefer? {list_of_genre}:")
rating = int(input("rating? "))

if genre == "mystery" and rating > 8:
    print(f"Recommended mystery Movie: {mystery_recommendation}")

if genre == "drama" or rating > 7:
    print(f"Recommended drama Movie: {drama_recommendation}")

if genre == "action" and rating < 6:
    print(f"Recommended Thriller Movie: {thriller_recommendation} ")

if genre not in list_of_genre:
    print(f"General Recommendation is: {general_recommendations}")
