count_of_days = int(input())
total_quantity_of_food = float(input())

total_biscuits_eaten = 0
total_food_eaten = 0
total_food_eaten_from_dog = 0
total_food_eaten_from_cat = 0

for day in range(1, count_of_days + 1):
    dog_food_grams_eaten = int(input())
    cat_food_grams_eaten = int(input())

    current_total_food_eaten = dog_food_grams_eaten + cat_food_grams_eaten

    if day % 3 == 0:
        total_biscuits_eaten += current_total_food_eaten * 0.1

    total_food_eaten += current_total_food_eaten
    total_food_eaten_from_dog += dog_food_grams_eaten
    total_food_eaten_from_cat += cat_food_grams_eaten

print(f"Total eaten biscuits: {round(total_biscuits_eaten)}gr.")
print(f"{(total_food_eaten / total_quantity_of_food * 100):.2f}% of the food has been eaten.")
print(f"{(total_food_eaten_from_dog / total_food_eaten * 100):.2f}% eaten from the dog.")
print(f"{(total_food_eaten_from_cat / total_food_eaten * 100):.2f}% eaten from the cat.")
