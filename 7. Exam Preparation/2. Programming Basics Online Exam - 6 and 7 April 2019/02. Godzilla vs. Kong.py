budget = float(input())
count_of_extras = int(input())
price_of_clothing_per_extra = float(input())

decor_price = budget * 0.1
price_for_extras = count_of_extras * price_of_clothing_per_extra

if count_of_extras > 150:
    price_for_extras -= price_for_extras * 0.1

total_price = decor_price + price_for_extras

if budget >= total_price:
    money_left = budget - total_price
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    money_needed = total_price - budget
    print('Not enough money!')
    print(f'Wingard needs {money_needed:.2f} leva more.')
