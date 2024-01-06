price_of_baggage_above_20_kg = float(input())
kg_of_baggage = float(input())
days_until_travelling = int(input())
count_of_baggage = int(input())

price_of_baggage = 0

if kg_of_baggage < 10:
    price_of_baggage = price_of_baggage_above_20_kg * 0.2
elif 10 <= kg_of_baggage <= 20:
    price_of_baggage = price_of_baggage_above_20_kg / 2
else:
    price_of_baggage = price_of_baggage_above_20_kg

if days_until_travelling < 7:
    price_of_baggage += price_of_baggage * 0.4
elif 7 <= days_until_travelling <= 30:
    price_of_baggage += price_of_baggage * 0.15
else:
    price_of_baggage += price_of_baggage * 0.1

total_price = count_of_baggage * price_of_baggage

print(f"The total price of bags is: {total_price:.2f} lv.")
