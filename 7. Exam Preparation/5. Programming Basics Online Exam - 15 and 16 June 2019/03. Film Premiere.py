projection = input()
type_of_packet = input()
number_of_tickets = int(input())

price_for_one = 0

if projection == "John Wick":
    if type_of_packet == "Drink":
        price_for_one = 12
    elif type_of_packet == "Popcorn":
        price_for_one = 15
    else:
        price_for_one = 19
elif projection == "Star Wars":
    if type_of_packet == "Drink":
        price_for_one = 18
    elif type_of_packet == "Popcorn":
        price_for_one = 25
    else:
        price_for_one = 30
else:
    if type_of_packet == "Drink":
        price_for_one = 9
    elif type_of_packet == "Popcorn":
        price_for_one = 11
    else:
        price_for_one = 14

total_price = price_for_one * number_of_tickets

if projection == "Star Wars" and  number_of_tickets >= 4:
    total_price -= total_price * 0.3
if projection == "Jumanji" and number_of_tickets == 2:
    total_price -= total_price * 0.15

print(f"Your bill is {total_price:.2f} leva.")
