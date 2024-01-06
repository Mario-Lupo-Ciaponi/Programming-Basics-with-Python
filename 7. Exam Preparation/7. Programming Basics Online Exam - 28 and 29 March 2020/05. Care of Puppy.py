quantity_of_food_in_kg = int(input())
quantity_of_food_in_gr = quantity_of_food_in_kg * 1000

command = input()
while command != "Adopted":
    quantity_of_food_in_gr -= int(command)
    command = input()

if quantity_of_food_in_gr < 0:
    print(f"Food is not enough. You need {abs(quantity_of_food_in_gr)} grams more.")
else:
    print(f"Food is enough! Leftovers: {quantity_of_food_in_gr} grams.")
