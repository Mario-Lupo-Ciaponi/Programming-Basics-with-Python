import math

number_of_guests = int(input())
budget = int(input())

number_of_kozunaks = math.ceil(number_of_guests / 3)
number_of_painted_eggs = number_of_guests * 2

price_for_kozunaks = number_of_kozunaks * 4
price_for_painted_eggs = number_of_painted_eggs * 0.45

total_price = price_for_kozunaks + price_for_painted_eggs

if budget >= total_price:
    money_left = budget - total_price

    print(f"Lyubo bought {number_of_kozunaks} Easter bread and {number_of_painted_eggs} eggs.")
    print(f"He has {money_left:.2f} lv. left.")
else:
    money_needed = total_price - budget

    print("Lyubo doesn't have enough money.")
    print(f"He needs {money_needed:.2f} lv. more.")
