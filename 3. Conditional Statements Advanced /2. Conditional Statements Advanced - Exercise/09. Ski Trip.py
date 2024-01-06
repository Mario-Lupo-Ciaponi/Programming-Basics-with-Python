count_of_days = int(input())
type_of_room = input()
feedback = input()

count_of_nights = count_of_days - 1
price = 0

if type_of_room == 'room for one person':
    price = count_of_nights * 18
elif type_of_room == 'apartment':
    price = count_of_nights * 25

    if count_of_days < 10:
        price -= price * 0.3
    elif count_of_days >= 10 and count_of_days  <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.5
else:
    price = count_of_nights * 35

    if count_of_days < 10:
        price -= price * 0.1
    elif count_of_days >= 10 and count_of_days <= 15:
        price -= price * 0.15
    else:
        price -= price * 0.2

if feedback == 'positive':
    price += price * 0.25
else:
    price -= price * 0.1

print(f'{price:.2f}')
