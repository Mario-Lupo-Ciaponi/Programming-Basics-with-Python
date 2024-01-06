country = input()
gymnastic_apparatus = input()

difficulty = 0
performance = 0

if country == 'Russia':
    if gymnastic_apparatus == 'ribbon':
        difficulty = 9.100
        performance = 9.400
    elif gymnastic_apparatus == 'hoop':
        difficulty = 9.300
        performance = 9.800
    else:
        difficulty = 9.600
        performance = 9.000
elif country == 'Bulgaria':
    if gymnastic_apparatus == 'ribbon':
        difficulty = 9.600
        performance = 9.400
    elif gymnastic_apparatus == 'hoop':
        difficulty = 9.550
        performance = 9.750
    else:
        difficulty = 9.500
        performance = 9.400
else:
    if gymnastic_apparatus == 'ribbon':
        difficulty = 9.200
        performance = 9.500
    elif gymnastic_apparatus == 'hoop':
        difficulty = 9.450
        performance = 9.350
    else:
        difficulty = 9.700
        performance = 9.150

total_points = difficulty + performance

percentage_from_hundred = 100 - (total_points / 20 * 100)

print(f'The team of {country} get {total_points:.3f} on {gymnastic_apparatus}.')
print(f'{percentage_from_hundred:.2f}%')
