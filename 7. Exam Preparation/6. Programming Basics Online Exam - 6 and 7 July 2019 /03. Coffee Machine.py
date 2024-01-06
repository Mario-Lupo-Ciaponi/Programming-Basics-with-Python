drink = input()
sugar = input()
number_of_drinks = int(input())

price_of_drink = 0

if drink == "Espresso":
    if sugar == "Without":
        price_of_drink = 0.9
    elif sugar == "Normal":
        price_of_drink = 1
    else:
        price_of_drink = 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price_of_drink = 1
    elif sugar == "Normal":
        price_of_drink = 1.2
    else:
        price_of_drink = 1.6
else:
    if sugar == "Without":
        price_of_drink = 0.5
    elif sugar == "Normal":
        price_of_drink = 0.6
    else:
        price_of_drink = 0.7

total_price = number_of_drinks * price_of_drink

if sugar == "Without":
    total_price -= total_price * 0.35
if drink == "Espresso" and number_of_drinks > 5:
    total_price -= total_price * 0.25
if total_price > 15:
    total_price -= total_price * 0.2

print(f"You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.")
