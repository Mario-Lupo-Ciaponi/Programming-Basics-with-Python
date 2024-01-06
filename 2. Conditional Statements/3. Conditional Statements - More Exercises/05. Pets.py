import math

count_of_days = int(input())
food_left_in_kg = int(input())

food_eaten_by_dog_per_day = float(input())
food_eaten_by_cat_per_day = float(input())
food_eaten_by_tortoise_per_day = float(input()) / 1000

total_food_needed_for_dog = count_of_days * food_eaten_by_dog_per_day
total_food_needed_for_cat = count_of_days * food_eaten_by_cat_per_day
total_food_needed_for_tortoise = count_of_days * food_eaten_by_tortoise_per_day

total_food_needed = total_food_needed_for_dog + total_food_needed_for_cat + total_food_needed_for_tortoise

if food_left_in_kg >= total_food_needed:
    food_left = food_left_in_kg - total_food_needed

    print(f'{math.floor(food_left)} kilos of food left.')
else:
    food_needed = total_food_needed - food_left_in_kg

    print(f'{math.ceil(food_needed)} more kilos of food are needed.')
