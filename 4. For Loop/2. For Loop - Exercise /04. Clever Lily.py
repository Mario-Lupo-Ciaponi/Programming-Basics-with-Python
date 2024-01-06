years_of_lily = int(input())
wash_machine_price = float(input())
price_per_toy = int(input())

count_of_toys = 0
count_money_bithdays = 1
money_from_birthday = 0

for year in range(1, years_of_lily + 1):
    if year % 2 != 0:
        count_of_toys += 1
    else:
        money_from_birthday += 10 * count_money_bithdays
        money_from_birthday -= 1

        count_money_bithdays += 1

money_from_toys = price_per_toy * count_of_toys

total_money = money_from_birthday + money_from_toys

if total_money >= wash_machine_price:
    money_left = total_money - wash_machine_price

    print(f'Yes! {money_left:.2f}')
else:
    money_needed = wash_machine_price - total_money

    print(f'No! {money_needed:.2f}')
