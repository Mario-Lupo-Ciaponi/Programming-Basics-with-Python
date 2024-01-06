budget = float(input())
number_os_series = int(input())

total_price = 0

for i in range(number_os_series):
    series_name = input()
    price = float(input())

    if series_name == "Thrones":
        price -= price * 0.5
    elif series_name == "Lucifer":
        price -= price * 0.4
    elif series_name == "Protector":
        price -= price * 0.3
    elif series_name == "TotalDrama":
        price -= price * 0.2
    elif series_name == "Area":
        price -= price * 0.1

    total_price += price

if budget >= total_price:
    money_left = budget - total_price
    print(f"You bought all the series and left with {money_left:.2f} lv.")
else:
    money_needed = total_price - budget
    print(f"You need {money_needed:.2f} lv. more to buy the series!")
