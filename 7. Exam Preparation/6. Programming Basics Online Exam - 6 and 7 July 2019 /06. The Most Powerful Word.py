import math
import sys

word = input()

biggest_points = -sys.maxsize
best_word = ""

while word != "End of words":
    first_letter = True
    points = 0

    for letter in word:
        points += ord(letter)

    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' \
       or word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
            points *= len(word)
    else:
        points = math.floor(points / len(word))

    if points >= biggest_points:
        biggest_points = points
        best_word = word

    word = input()

print(f"The most powerful word is {best_word} - {biggest_points}")
