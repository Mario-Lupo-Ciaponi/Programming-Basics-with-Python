budget = float(input())
season = input()

price = 0
class_of_car = ''
type_of_car = ''

if budget <= 100:
    class_of_car = 'Economy class'

    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.35
    else:
        type_of_car = 'Jeep'
        price = budget * 0.65
elif 100 < budget <= 500:
    class_of_car = 'Compact class'

    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.45
    else:
        type_of_car = 'Jeep'
        price = budget * 0.80
else:
    class_of_car = 'Luxury class'

    type_of_car = 'Jeep'
    price = budget * 0.9

print(class_of_car)
print(f'{type_of_car} - {price:.2f}')
