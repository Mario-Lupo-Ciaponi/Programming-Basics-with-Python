import math

change = float(input())

change_in_coins = math.floor(change * 100)

coins_count_to_change = 0

while change_in_coins > 0:
    if change_in_coins >= 200:
        change_in_coins -= 200
    elif 100 <= change_in_coins < 200:
        change_in_coins -= 100
    elif 50 <= change_in_coins < 100:
        change_in_coins -= 50
    elif 20 <= change_in_coins < 50:
        change_in_coins -= 20
    elif 10 <= change_in_coins < 20:
        change_in_coins -= 10
    elif 5 <= change_in_coins < 10:
        change_in_coins -= 5
    elif 2 <= change_in_coins < 5:
        change_in_coins -= 2
    else:
        change_in_coins -= 1

    coins_count_to_change += 1

print(coins_count_to_change)
