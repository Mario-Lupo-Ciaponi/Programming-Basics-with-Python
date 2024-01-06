budget = int(input())
season = input()
count_of_fisherman = int(input())

boat_price = 0

if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
else:
    boat_price = 2600

if count_of_fisherman <= 6:
    boat_price -= boat_price * 0.1
elif count_of_fisherman > 7 and count_of_fisherman <= 11:
    boat_price -= boat_price * 0.15
else:
    boat_price -= boat_price * 0.25

if count_of_fisherman % 2 == 0 and season != 'Autumn':
    boat_price -= boat_price * 0.05

if budget >= boat_price:
    money_left = budget - boat_price
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = boat_price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')
