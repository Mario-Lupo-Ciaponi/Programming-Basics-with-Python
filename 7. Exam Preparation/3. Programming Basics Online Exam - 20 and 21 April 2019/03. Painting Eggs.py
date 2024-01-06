size_of_eggs = input()
color = input()
number_of_eggs = int(input())

price_per_egg = 0

if size_of_eggs == "Large":
    if color == "Red":
        price_per_egg = 16
    elif color == "Green":
        price_per_egg = 12
    else:
        price_per_egg = 9
elif size_of_eggs == "Medium":
    if color == "Red":
        price_per_egg = 13
    elif color == "Green":
        price_per_egg = 9
    else:
        price_per_egg = 7
else:
    if color == "Red":
        price_per_egg = 9
    elif color == "Green":
        price_per_egg = 8
    else:
        price_per_egg = 5

total_price = number_of_eggs * price_per_egg
total_price -= total_price * 0.35

print(f"{total_price:.2f} leva.")
