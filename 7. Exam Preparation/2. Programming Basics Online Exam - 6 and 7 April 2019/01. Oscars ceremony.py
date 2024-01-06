rent_for_hall = int(input())

price_for_statues = rent_for_hall - rent_for_hall * 0.3
price_for_kettering = price_for_statues - price_for_statues * 0.15
voicing_price = price_for_kettering / 2

total_price = rent_for_hall + price_for_statues + price_for_kettering + voicing_price

print(f"{total_price:.2f}")
