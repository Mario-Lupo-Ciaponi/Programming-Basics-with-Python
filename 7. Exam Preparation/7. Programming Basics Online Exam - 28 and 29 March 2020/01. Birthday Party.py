rent_for_hall = float(input())

cake_price = rent_for_hall * 0.2
beverages_price = cake_price - cake_price * 0.45
animator_price = rent_for_hall / 3

total_price = rent_for_hall + cake_price + beverages_price + animator_price

print(total_price)
