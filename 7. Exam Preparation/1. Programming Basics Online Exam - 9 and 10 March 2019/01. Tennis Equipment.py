import math

price_per_tennis_racket = float(input())
count_of_tennis_rackets = int(input())
count_of_pairs_of_shoes = int(input())

price_of_rackets = count_of_tennis_rackets * price_per_tennis_racket

price_per_pair_of_shoes = price_per_tennis_racket / 6
price_of_shoes = count_of_pairs_of_shoes * price_per_pair_of_shoes

price_of_other_equipment = (price_of_rackets + price_of_shoes) * 0.2

total_price = price_of_rackets + price_of_shoes + price_of_other_equipment

total_price_of_djokovic = total_price / 8
total_price_of_sponsors = total_price * 7 / 8

print(f'Price to be paid by Djokovic {math.floor(total_price_of_djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(total_price_of_sponsors)}')
