import math

vineyard_qubic_meters = int(input())
grape_per_qubic_meter = float(input())
liters_needed = int(input())
workers_count = int(input())

vineyard_for_wine = vineyard_qubic_meters * 0.4

total_grape = vineyard_for_wine * grape_per_qubic_meter
total_wine = total_grape / 2.5

if total_wine >= liters_needed:
    wine_left = total_wine - liters_needed

    print(f'Good harvest this year! Total wine: {math.floor(total_wine)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_left / workers_count)} liters per person.')
else:
    wine_needed = liters_needed - total_wine

    print(f'It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.')
