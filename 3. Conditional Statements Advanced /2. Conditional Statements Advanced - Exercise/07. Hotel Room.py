month = input()
count_of_nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = count_of_nights * 50
    apartment_price = count_of_nights * 65

    if count_of_nights > 7 and count_of_nights <= 14:
        studio_price -= studio_price * 0.05
    elif count_of_nights > 14:
        studio_price -= studio_price * 0.3
elif month == 'June' or month == 'September':
    studio_price = count_of_nights * 75.2
    apartment_price = count_of_nights * 68.7

    if count_of_nights > 14:
        studio_price -= studio_price * 0.2
elif month == 'July' or month == 'August':
    studio_price = count_of_nights * 76
    apartment_price = count_of_nights * 77

if count_of_nights > 14:
    apartment_price -= apartment_price * 0.1

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
