movieGenre = input("Movie genre: ")
rating = 0

if movieGenre == "Action":
    newRating1 = int(input("Rate the movie The matrix: "))

if movieGenre == "Action" and newRating1 >= 8:
        print("You like action movies here's a Movie Recommendation: Avengers: Endgame")

if movieGenre == "Comedy":
    newRating2 = int(input("Rate the movie White Chicks: "))

if movieGenre == "Comedy" and newRating2 >= 7:
    print("You like comedy here's a Movie Recommendation: Three Amigos!")

if movieGenre == "Romance":
    newRating3 = int(input("Rate the movie The Notebook: "))

if movieGenre == "Romance" and newRating3 < 6:
    print("Seems that you are not interested with romance here's a thriller movie: Parasite")

if movieGenre == "Action" and newRating1 < 8:
    print("Seems that you are not interested with action movies here's a fantasy movie: Wonka")

if movieGenre == "Comedy" and newRating2 < 7:
    print("Seems that you are not interested with comedy here's a horror movie: The Exorcist")

if movieGenre == "Romance" and newRating3 >= 6:
    print("You like Romance here's a Movie Recommendation: 365 days")
