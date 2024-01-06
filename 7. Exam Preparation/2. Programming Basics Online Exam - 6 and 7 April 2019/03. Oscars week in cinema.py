movie_name = input()
hall = input()
tickets_bought = int(input())

price_per_ticket = 0

if movie_name == "A Star Is Born":
    if hall == "normal":
        price_per_ticket = 7.5
    elif hall == "luxury":
        price_per_ticket = 10.5
    else:
        price_per_ticket = 13.5
elif movie_name == "Bohemian Rhapsody":
    if hall == "normal":
        price_per_ticket = 7.35
    elif hall == "luxury":
        price_per_ticket = 9.45
    else:
        price_per_ticket = 12.75
elif movie_name == "Green Book":
    if hall == "normal":
        price_per_ticket = 8.15
    elif hall == "luxury":
        price_per_ticket = 10.25
    else:
        price_per_ticket = 13.25
else:
    if hall == "normal":
        price_per_ticket = 8.75
    elif hall == "luxury":
        price_per_ticket = 11.55
    else:
        price_per_ticket = 13.95

total_price = tickets_bought * price_per_ticket

print(f"{movie_name} -> {total_price:.2f} lv.")
