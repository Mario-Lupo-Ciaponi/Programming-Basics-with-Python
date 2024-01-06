type_of_flowers = input()
count_of_flowers = int(input())
budget = int(input())
price = 0

if type_of_flowers == 'Roses':
    price = count_of_flowers * 5

    if count_of_flowers > 80:
        price -= price * 0.1
elif type_of_flowers == 'Dahlias':
    price = count_of_flowers * 3.8

    if count_of_flowers > 90:
        price -= price * 0.15
elif type_of_flowers == 'Tulips':
    price = count_of_flowers * 2.8

    if count_of_flowers > 80:
        price -= price * 0.15
elif type_of_flowers == 'Narcissus':
    price = count_of_flowers * 3

    if count_of_flowers < 120:
        price += price * 0.15
else:
    price = count_of_flowers * 2.5

    if count_of_flowers < 80:
        price += price * 0.2

if budget >= price:
    money_left = budget - price
    print(f'Hey, you have a great garden with {count_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.')
else:
    money_needed = price - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')
