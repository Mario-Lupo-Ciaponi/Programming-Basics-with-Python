budget = float(input())
destination = input()
season = input()
count_of_days = int(input())

price = 0

if destination == "Dubai":
    if season == "Winter":
        price = count_of_days * 45000
    else:
        price = count_of_days * 40000

    price -= price * 0.3
elif destination == "Sofia":
    if season == "Winter":
        price = count_of_days * 17000
    else:
        price = count_of_days * 12500

    price += price * 0.25
else:
    if season == "Winter":
        price = count_of_days * 24000
    else:
        price = count_of_days * 20250

if budget >= price:
    money_left = budget - price
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
else:
    money_needed = price - budget
    print(f"The director needs {money_needed:.2f} leva more!")
