count_of_easter_breads_for_rating = int(input())

winner_name = ""
winner_points = 0

for i in range(count_of_easter_breads_for_rating):
    baker_name = input()

    total_points = 0
    command = input()
    while command != "Stop":
        points = int(command)
        total_points += points

        command = input()

    print(f"{baker_name} has {total_points} points.")

    if total_points > winner_points:
        print(f"{baker_name} is the new number 1!")

        winner_name = baker_name
        winner_points = total_points

print(f"{winner_name} won competition with {winner_points} points!")
