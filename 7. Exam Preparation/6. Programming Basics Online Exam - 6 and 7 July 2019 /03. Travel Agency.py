import sys

town = input()
packet = input()
vip_discount = input()
count_of_days = int(input())

if count_of_days < 1:
    print("Days must be positive number!")
    sys.exit()

price_per_day = 0
discount = False

vip_discount_percent = 0

invalid = False

if count_of_days > 7:
    discount = True

if town == "Bansko" or town == "Borovets":
    if packet == "noEquipment":
        price_per_day = 80

        if vip_discount == "yes":
            vip_discount_percent = 5
    elif packet == "withEquipment":
        price_per_day = 100

        if vip_discount == "yes":
            vip_discount_percent = 10
    else:
        invalid = True
elif town == "Varna" or town == "Burgas":
    if packet == "noBreakfast":
        price_per_day = 100

        if vip_discount == "yes":
            vip_discount_percent = 7
    elif packet == "withBreakfast":
        price_per_day = 130

        if vip_discount == "yes":
            vip_discount_percent = 12
    else:
        invalid = True
else:
    invalid = True

if invalid:
    print("Invalid input!")
    sys.exit()

total_price = count_of_days * price_per_day

if discount:
    total_price -= price_per_day

if vip_discount == "yes":
    total_price -= total_price * (vip_discount_percent / 100)

print(f"The price is {total_price:.2f}lv! Have a nice time!")
