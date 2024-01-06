import math

magnolias_count = int(input())
hyacinths_count = int(input())
rosses_count = int(input())
cacti_count = int(input())

gift_price = float(input())

money_earned_from_magnolias = magnolias_count * 3.25
money_earned_from_hyacinths = hyacinths_count * 4
money_earned_from_rosses = rosses_count * 3.5
money_earned_from_cacti = cacti_count * 8

total_money_earned = money_earned_from_magnolias + money_earned_from_hyacinths + money_earned_from_rosses + money_earned_from_cacti

total_money_earned -= total_money_earned * 0.05

if total_money_earned >= gift_price:
    money_left = math.floor(total_money_earned - gift_price)

    print(f'She is left with {money_left} leva.')
else:
    money_needed = math.ceil(gift_price - total_money_earned)

    print(f'She will have to borrow {money_needed} leva.')
