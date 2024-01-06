import math
import sys

count_of_eater_breads = int(input())

most_sugar_used = -sys.maxsize
most_flour_used = -sys.maxsize

total_grams_of_sugar = 0
total_grams_of_flour = 0

for i in range(count_of_eater_breads):
    grams_of_sugar = int(input())
    grams_of_flour = int(input())

    if grams_of_sugar > most_sugar_used:
        most_sugar_used = grams_of_sugar
    if grams_of_flour > most_flour_used:
        most_flour_used = grams_of_flour

    total_grams_of_sugar += grams_of_sugar
    total_grams_of_flour += grams_of_flour

print(f"Sugar: {math.ceil(total_grams_of_sugar / 950)}")
print(f"Flour: {math.ceil(total_grams_of_flour / 750)}")
print(f"Max used flour is {most_flour_used} grams, max used sugar is {most_sugar_used} grams.")
