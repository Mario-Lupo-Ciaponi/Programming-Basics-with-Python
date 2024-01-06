budget = float(input())
season = input()

accomodation = ''
price = 0
destination = ''

if budget <= 100:
    destination = 'Bulgaria'

    if season == 'summer':
        accomodation = 'Camp'
        price = budget * 0.3
    else:
        accomodation = 'Hotel'
        price = budget * 0.7
elif budget > 100 and budget <= 1000:
    destination = 'Balkans'

    if season == 'summer':
        accomodation = 'Camp'
        price = budget * 0.4
    else:
        accomodation = 'Hotel'
        price = budget * 0.8
else:
    destination = 'Europe'
    accomodation = 'Hotel'

    price = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{accomodation} - {price:.2f}')
