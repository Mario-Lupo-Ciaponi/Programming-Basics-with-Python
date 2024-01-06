price_of_strawberries = float(input())
price_of_raspberries = price_of_strawberries / 2
price_of_oranges = price_of_raspberries - price_of_raspberries * 0.4
price_of_bananas = price_of_raspberries - price_of_raspberries * 0.8

kg_of_bananas = float(input())
kg_of_oranges = float(input())
kg_of_raspberries = float(input())
kg_of_strawberries = float(input())

total_price_of_strawberries = kg_of_strawberries * price_of_strawberries
total_price_of_raspberries = kg_of_raspberries * price_of_raspberries
total_price_of_oranges = kg_of_oranges * price_of_oranges
total_price_of_bananas = kg_of_bananas * price_of_bananas

total_price = total_price_of_strawberries + total_price_of_raspberries + total_price_of_oranges + total_price_of_bananas

print(f"{total_price:.2f}")
