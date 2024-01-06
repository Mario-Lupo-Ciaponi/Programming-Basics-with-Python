stage_of_finals = input()
type_of_ticket = input()
number_of_tickets = int(input())
photo_with_trophy = input()

price = 0

photo = 40
price_for_photo = True

if type_of_ticket == 'Standard':
    if stage_of_finals == 'Quarter final':
        price = number_of_tickets * 55.5
    elif stage_of_finals == 'Semi final':
        price = number_of_tickets * 75.88
    else:
        price = number_of_tickets * 110.1
elif type_of_ticket == 'Premium':
    if stage_of_finals == 'Quarter final':
        price = number_of_tickets * 105.2
    elif stage_of_finals == 'Semi final':
        price = number_of_tickets * 125.22
    else:
        price = number_of_tickets * 160.66
else:
    if stage_of_finals == 'Quarter final':
        price = number_of_tickets * 118.9
    elif stage_of_finals == 'Semi final':
        price = number_of_tickets * 300.4
    else:
        price = number_of_tickets * 400

if 2500 <= price <= 4000:
    price -= price * 0.1
elif price > 4000:
    price -= price * 0.25
    price_for_photo = False

if photo_with_trophy == 'Y' and price_for_photo:
    price += number_of_tickets * photo

print(f'{price:.2f}')
