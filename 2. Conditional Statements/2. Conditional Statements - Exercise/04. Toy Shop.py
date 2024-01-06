trip_price = float(input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

count_of_toys = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

puzzles_profit = puzzles_count * 2.6
talking_dolls_profit = talking_dolls_count * 3
teddy_bears_profit = teddy_bears_count * 4.1
minions_profit = minions_count * 8.2
trucks_profit = trucks_count * 2

rent_percent = 10

total_profit = puzzles_profit + talking_dolls_profit + teddy_bears_profit + minions_profit + trucks_profit

if count_of_toys >= 50:
    total_profit -= total_profit * 0.25

total_profit -= total_profit * (rent_percent / 100)

if total_profit >= trip_price:
    money_left = total_profit - trip_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = trip_price - total_profit
    print(f'Not enough money! {money_needed:.2f} lv needed.')
