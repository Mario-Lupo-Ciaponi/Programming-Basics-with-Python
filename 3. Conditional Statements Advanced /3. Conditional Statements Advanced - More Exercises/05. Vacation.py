budget = float(input())
season = input()

price = 0
accommodation = ''
country = ''

if budget <= 1000:
    accommodation = 'Camp'

    if season == 'Summer':
        country = 'Alaska'
        price = budget * 0.65
    else:
        country = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = 'Hut'

    if season == 'Summer':
        country = 'Alaska'
        price = budget * 0.8
    else:
        country = 'Morocco'
        price = budget * 0.6
else:
    accommodation = 'Hotel'

    if season == 'Summer':
        country = 'Alaska'
    else:
        country = 'Morocco'

    price = budget * 0.9

print(f'{country} - {accommodation} - {price:.2f}')
