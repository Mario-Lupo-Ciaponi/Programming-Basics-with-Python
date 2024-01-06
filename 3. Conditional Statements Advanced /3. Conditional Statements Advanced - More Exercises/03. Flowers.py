count_of_chrysanthemums = int(input())
count_of_rosses = int(input())
count_of_tulips = int(input())
season = input()
holiday = input()

bouquet_price = 0

if season == 'Spring' or season == 'Summer':
    bouquet_price = (count_of_chrysanthemums * 2) + (count_of_rosses * 4.1) + (count_of_tulips * 2.5)

    if holiday == 'Y':
        bouquet_price += bouquet_price * 0.15

    if season == 'Spring' and count_of_tulips > 7:
        bouquet_price -= bouquet_price * 0.05
elif season == 'Autumn' or season == 'Winter':
    bouquet_price = (count_of_chrysanthemums * 3.75) + (count_of_rosses * 4.5) + (count_of_tulips * 4.15)

    if holiday == 'Y':
        bouquet_price += bouquet_price * 0.15

    if season == 'Winter' and count_of_rosses >= 10:
        bouquet_price -= bouquet_price * 0.1

if count_of_chrysanthemums + count_of_rosses + count_of_tulips > 20:
    bouquet_price -= bouquet_price * 0.2

print(f'{(bouquet_price + 2):.2f}')
