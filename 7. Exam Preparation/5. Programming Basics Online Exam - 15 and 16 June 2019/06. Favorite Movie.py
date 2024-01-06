import sys

movie = input()

best_movie_name = ""
max_sum = -sys.maxsize
counter = 0

while movie != "STOP":
    sum = 0
    counter += 1

    if counter == 7:
        print("The limit is reached.")
        break

    for letter in movie:
        if letter.islower():
            sum += ord(letter) - (2 * len(movie))
        elif letter.isupper():
            sum += ord(letter) - len(movie)
        else:
            sum += ord(letter)

    if sum > max_sum:
        best_movie_name = movie
        max_sum = sum

    movie = input()

print(f"The best movie for you is {best_movie_name} with {max_sum} ASCII sum.")
