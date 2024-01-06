budget = float(input())

count_of_videocards = int(input())
count_of_processors = int(input())
count_of_ram = int(input())

price_of_videocards = count_of_videocards * 250
price_of_processors = count_of_processors * (price_of_videocards * 0.35)
price_of_ram = count_of_ram * (price_of_videocards * 0.1)

total_price = price_of_videocards + price_of_processors + price_of_ram

if count_of_videocards > count_of_processors:
    total_price -= total_price * 0.15

if budget >= total_price:
    money_left = budget - total_price
    print(f'You have {money_left:.2f} leva left!')
else:
    money_needed = total_price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva more!')
    