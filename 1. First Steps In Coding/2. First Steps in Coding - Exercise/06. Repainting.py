quantity_of_nailon = int(input())
quantity_of_paint = int(input())
quantity_of_thinner = int(input())
hours_of_work = int(input())

extra_nailon = quantity_of_nailon + 2
extra_paint = quantity_of_paint + quantity_of_paint * 0.1

price_of_nailon = extra_nailon * 1.5
price_of_paint = extra_paint * 14.5
price_of_thinner = quantity_of_thinner * 5
price_of_bags = 0.4

total_price_of_materials = price_of_nailon + price_of_paint + price_of_thinner + price_of_bags

price_for_workers_per_hour = total_price_of_materials * 0.3
total_price_of_workers = price_for_workers_per_hour * hours_of_work

total_price = total_price_of_materials + total_price_of_workers

print(total_price)
