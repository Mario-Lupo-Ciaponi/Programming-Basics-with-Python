number_of_guests = int(input())
envelope_price_per_guest = float(input())
budget = float(input())

if 10 <= number_of_guests <= 15:
    envelope_price_per_guest -= envelope_price_per_guest * 0.15
elif 15 < number_of_guests <= 20:
    envelope_price_per_guest -= envelope_price_per_guest * 0.2
elif number_of_guests > 20:
    envelope_price_per_guest -= envelope_price_per_guest * 0.25

cake_price = budget * 0.1

envelope_price = number_of_guests * envelope_price_per_guest
total_price = envelope_price + cake_price

if budget >= total_price:
    money_left = budget - total_price
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    print(f"No party! {money_needed:.2f} leva needed.")
