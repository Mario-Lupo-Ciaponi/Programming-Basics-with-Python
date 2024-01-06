import sys

number_of_movies = int(input())

highest_rating = -sys.maxsize
highest_movie_rating = ""

lowest_rating = sys.maxsize
lowest_movie_rating = ""

average_rating = 0

for i in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_movie_rating = movie_name
    if movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_movie_rating = movie_name

    average_rating += movie_rating

print(f"{highest_movie_rating} is with highest rating: {round(highest_rating, 1)}")
print(f"{lowest_movie_rating} is with lowest rating: {round(lowest_rating, 1)}")
print(f"Average rating: {round((average_rating / number_of_movies), 1)}")
