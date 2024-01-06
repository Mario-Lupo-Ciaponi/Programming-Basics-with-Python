price_of_flour_per_kg = float(input())
price_of_sugar_per_kg = price_of_flour_per_kg - price_of_flour_per_kg * 0.25
price_of_single_crust = price_of_flour_per_kg + price_of_flour_per_kg * 0.1
price_of_yeast_per_packet = price_of_sugar_per_kg - price_of_sugar_per_kg * 0.8

kg_of_flour = float(input())
kg_of_sugar = float(input())
count_of_crusts = int(input())
packets_of_yeast = int(input())

price_of_flour = kg_of_flour * price_of_flour_per_kg
price_of_sugar = kg_of_sugar * price_of_sugar_per_kg
price_of_crust = count_of_crusts * price_of_single_crust
price_of_yeast = packets_of_yeast * price_of_yeast_per_packet

total_price = price_of_flour + price_of_sugar + price_of_crust + price_of_yeast

print(f"{total_price:.2f}")
