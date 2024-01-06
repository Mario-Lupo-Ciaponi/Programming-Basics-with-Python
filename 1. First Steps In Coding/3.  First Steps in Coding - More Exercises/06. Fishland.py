mackerel_price_per_kg = float(input())
sprat_price_per_kg = float(input())

kilograms_of_bonito = float(input())
kilograms_of_safrid = float(input())
kilograms_of_mussels = float(input())

bonito_price_per_kg = mackerel_price_per_kg + mackerel_price_per_kg * 0.6
safrid_price_per_kg = sprat_price_per_kg + sprat_price_per_kg * 0.8
mussels_price_per_kg = 7.5

bonito_total_price = kilograms_of_bonito * bonito_price_per_kg
safrid_total_price = kilograms_of_safrid * safrid_price_per_kg
mussels_total_price = kilograms_of_mussels * mussels_price_per_kg

total_price = bonito_total_price + safrid_total_price + mussels_total_price

print(f'{total_price:.2f}')
