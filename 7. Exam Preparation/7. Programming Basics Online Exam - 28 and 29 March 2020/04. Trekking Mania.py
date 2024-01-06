number_of_groups = int(input())

musalla_climber_groups = 0
mont_blanc_climber_groups = 0
kilimanjaro_climber_groups = 0
k2_climber_groups = 0
everest_climber_groups = 0

count_of_climbers = 0

for group in range(number_of_groups):
    quantity_of_group = int(input())

    if quantity_of_group <= 5:
        musalla_climber_groups += quantity_of_group
    elif 6 <= quantity_of_group <= 12:
        mont_blanc_climber_groups += quantity_of_group
    elif 13 <= quantity_of_group <= 25:
        kilimanjaro_climber_groups += quantity_of_group
    elif 26 <= quantity_of_group <= 40:
        k2_climber_groups += quantity_of_group
    else:
        everest_climber_groups += quantity_of_group

    count_of_climbers += quantity_of_group

musalla_percentage = musalla_climber_groups / count_of_climbers * 100
mont_blanc_percentage = mont_blanc_climber_groups / count_of_climbers * 100
kilimanjaro_percentage = kilimanjaro_climber_groups / count_of_climbers * 100
k2_climber_percentage = k2_climber_groups / count_of_climbers * 100
everest_percentage = everest_climber_groups / count_of_climbers * 100

print(f'{musalla_percentage:.2f}%')
print(f'{mont_blanc_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_climber_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')
