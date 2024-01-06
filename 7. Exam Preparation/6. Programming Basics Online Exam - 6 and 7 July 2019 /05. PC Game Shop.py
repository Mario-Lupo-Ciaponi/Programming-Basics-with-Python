games_sold = int(input())

hearthstone_count = 0
fornite_count = 0
overwatch_count = 0
others_count = 0

for i in range(games_sold):
    game = input()

    if game == "Hearthstone":
        hearthstone_count += 1
    elif game == "Fornite":
        fornite_count += 1
    elif game == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_percent = hearthstone_count / games_sold * 100
fornite_percent = fornite_count / games_sold * 100
overwatch_percent = overwatch_count / games_sold * 100
others_percent = others_count / games_sold * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
