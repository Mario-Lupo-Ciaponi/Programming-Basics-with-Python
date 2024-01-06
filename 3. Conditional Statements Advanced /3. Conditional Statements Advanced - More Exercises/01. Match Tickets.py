budget = float(input())
category = input()
people_in_group = int(input())

price = 0

if category == 'VIP':
    price = people_in_group * 499.99
else:
    price = people_in_group * 249.99

if people_in_group <= 4:
    price += budget * 0.75
elif 5 <= people_in_group <= 9:
    price += budget * 0.6
elif 10 <= people_in_group <= 24:
    price += budget * 0.5
elif 25 <= people_in_group <= 49:
    price += budget * 0.4
else:
    price += budget * 0.25

if budget >= price:
    money_left = budget - price
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')
