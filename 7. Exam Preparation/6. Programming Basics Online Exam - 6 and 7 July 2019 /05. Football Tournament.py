import sys

team_name = input()
games_played = int(input())

total_points = 0

games_won = 0
games_in_tie = 0
games_lost = 0

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
    sys.exit()

for i in range(games_played):
    game_result = input()

    if game_result == "W":
        total_points += 3
        games_won += 1
    elif game_result == "D":
        total_points += 1
        games_in_tie += 1
    else:
        games_lost += 1

win_rate = games_won / games_played * 100

print(f"{team_name} has won {total_points} points during this season")
print("Total stats:")
print(f"## W: {games_won}")
print(f"## D: {games_in_tie}")
print(f"## L: {games_lost}")
print(f"Win rate: {win_rate:.2f}%")
