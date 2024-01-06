matches_won = 0
matches_lost = 0

total_matches = 0

squad_name = input()
while squad_name != "End of tournaments":
    number_of_matches = int(input())
    total_matches += number_of_matches

    match = 1
    for i in range(number_of_matches):
        first_score = int(input())
        second_score = int(input())

        if first_score > second_score:
            print(f"Game {match} of tournament {squad_name}: win with {first_score - second_score} points.")
            matches_won += 1
        else:
            print(f"Game {match} of tournament {squad_name}: lost with {second_score - first_score} points.")
            matches_lost += 1

        match += 1

    squad_name = input()

print(f"{(matches_won * 1.00 / total_matches * 100):.2f}% matches win")
print(f"{(matches_lost * 1.00 / total_matches * 100):.2f}% matches lost")
