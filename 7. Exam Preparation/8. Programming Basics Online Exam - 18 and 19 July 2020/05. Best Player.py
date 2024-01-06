import sys

best_player = ""
most_goals = -sys.maxsize
het_trick = False

name_of_player = input()

while name_of_player != "END":
    goals = int(input())

    if goals >= 10:
        best_player = name_of_player
        most_goals = goals
        het_trick = True

        break

    if goals > most_goals:
        best_player = name_of_player
        most_goals = goals

        if goals >= 3:
            het_trick = True
        else:
            het_trick = False

    name_of_player = input()

print(f"{best_player} is the best player!")

if het_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
