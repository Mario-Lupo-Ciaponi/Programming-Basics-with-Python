price_of_vegetable_per_kilogram = float(input())
price_of_fruit_per_kilogram = float(input())

kilograms_of_vegetable = int(input())
kilograms_of_fruit = int(input())

price_of_vegetables = kilograms_of_vegetable * price_of_vegetable_per_kilogram
price_of_fruits = kilograms_of_fruit * price_of_fruit_per_kilogram

total_price_in_leva = price_of_vegetables + price_of_fruits
total_price_in_euro = total_price_in_leva / 1.94

print(f'{total_price_in_euro:.2f}')
