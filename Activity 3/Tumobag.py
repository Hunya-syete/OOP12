print("Welcome to the Movie Recommender!")

# User's genre preference 
genre_preference = input("What genre do you prefer (action, comedy, romance, or other)? ").lower()

# User's rating preference 
rating_preference = int(input("On a scale of 1 to 10, how much do you value high ratings? "))

# Recommendations 
if genre_preference == "action" and rating_preference > 8:
   print("You might watch an action blockbuster like The Avengers or Mad Max: Fury Road")

elif genre_preference == "comedy" or rating_preference > 7:
   print("Here are the funny movies to brighten your day : Little Man or Bridesmaids")

elif genre_preference != "romance" and rating_preference < 6:
   print("A thrilling recommendation for you : The Silence of the Lambs, The Sixth Sense or Inception")

else:
   print("Here are some general recommendations that might suit you : Fast X, The Godfather,The Dark Knight")
       


print("Have fun and enjoy!")
