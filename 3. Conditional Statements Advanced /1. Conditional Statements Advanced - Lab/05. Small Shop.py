product = input()
town = input()
quantity = float(input())
price = 0

if town == 'Sofia':
    if product == 'coffee':
        price = quantity * 0.5
    elif product == 'water':
        price = quantity * 0.8
    elif product == 'beer':
        price = quantity * 1.2
    elif product == 'sweets':
        price = quantity * 1.45
    else:
        price = quantity * 1.6
elif town == 'Plovdiv':
    if product == 'coffee':
        price = quantity * 0.4
    elif product == 'water':
        price = quantity * 0.7
    elif product == 'beer':
        price = quantity * 1.15
    elif product == 'sweets':
        price = quantity * 1.3
    else:
        price = quantity * 1.5
else:
    if product == 'coffee':
        price = quantity * 0.45
    elif product == 'water':
        price = quantity * 0.7
    elif product == 'beer':
        price = quantity * 1.1
    elif product == 'sweets':
        price = quantity * 1.35
    else:
        price = quantity * 1.55

print(price)
