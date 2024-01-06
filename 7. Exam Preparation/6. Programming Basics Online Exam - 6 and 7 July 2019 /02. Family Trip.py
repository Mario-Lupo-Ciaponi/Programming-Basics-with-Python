budget = float(input())

count_of_nights = int(input())
price_per_night = float(input())
additional_expenses_percent = int(input())

if count_of_nights > 7:
    price_per_night -= price_per_night * 0.05

price_of_nights = count_of_nights * price_per_night
additional_expenses_price = budget * (additional_expenses_percent / 100)

total_price = price_of_nights + additional_expenses_price

if budget >= total_price:
    money_left = budget - total_price
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_needed = total_price - budget
    print(f"{money_needed:.2f} leva needed.")
