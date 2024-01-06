import math

number_of_people = int(input())

entrance_fee = float(input())
price_per_sun_lounger = float(input())
price_per_umbrella = float(input())

count_of_umbrellas = math.ceil(number_of_people / 2)
count_of_sun_loungers = math.ceil(number_of_people * 0.75)

total_price_of_fee = number_of_people * entrance_fee
total_price_of_umbrellas = count_of_umbrellas * price_per_umbrella
total_price_of_sun_loungers = count_of_sun_loungers * price_per_sun_lounger

total_price = total_price_of_fee + total_price_of_umbrellas + total_price_of_sun_loungers

print(f"{total_price:.2f} lv.")
