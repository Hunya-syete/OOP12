# to recommend movies
action_movies = ["The Matrix", "Avengers"]
comedy_movies = ["Superbad", "The Hangover"]
thriller_movies = ["Seven", "Leave the World Behind"]
list_of_genre = "[Action, Comedy or Thriller]"

# introduction
genre = input(f"What movie genre do you prefer? {list_of_genre}:")
rating = float(input("Rating do you prefer [0-10]: "))

# genre ratings
if genre == "Action" and rating > 8:
    print(f"Recommended Action Movie: {action_movies}")

if genre == "Comedy" or rating > 7:
    print(f"Recommended Comedy Movie: {comedy_movies}")

elif genre != "thriller" and rating < 6:
    print(f"Recommended Thriller Movie: {thriller_movies} ")

# general recommendation
else:
    print("Sorry, no specific recommendations. Try exploring popular movies!")

general_recommendations = ["Forrest Gump"]
print(f"General Recommendation:) {general_recommendations}")

# end
print("")
print("Thank you for using this code for your movie recommendations.")
