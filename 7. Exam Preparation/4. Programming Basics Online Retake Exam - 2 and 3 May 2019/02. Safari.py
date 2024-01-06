budget = float(input())
liters_needed = float(input())
day_of_the_week = input()

tour_guide_price = 100
price_of_fuel = liters_needed * 2.1

total_price = price_of_fuel + tour_guide_price

if day_of_the_week == "Saturday":
    total_price -= total_price * 0.1
else:
    total_price -= total_price * 0.2

if budget >= total_price:
    money_left = budget - total_price

    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_needed = total_price - budget

    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")
