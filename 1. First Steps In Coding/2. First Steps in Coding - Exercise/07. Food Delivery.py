count_of_chicken_menus = int(input())
count_of_fish_menus = int(input())
count_of_vegetarian_menus = int(input())

price_of_chicken_menus = count_of_chicken_menus * 10.35
price_of_fish_menus = count_of_fish_menus * 12.4
price_of_vegetarian_menus = count_of_vegetarian_menus * 8.15
delivery_price = 2.5

price_of_menus = price_of_chicken_menus + price_of_fish_menus + price_of_vegetarian_menus
price_of_desert_menus = price_of_menus * 0.2

total_price = price_of_menus + price_of_desert_menus + delivery_price

print(total_price)
