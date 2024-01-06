eggs_of_first_player = int(input())
eggs_of_second_player = int(input())

winner_is_first_player = False
winner_is_second_player = False

winner = input()
while winner != "End":
    if winner == "one":
        eggs_of_second_player -= 1
    else:
        eggs_of_first_player -= 1

    if eggs_of_first_player == 0:
        winner_is_second_player = True
        break
    elif eggs_of_second_player == 0:
        winner_is_first_player = True
        break

    winner = input()

if winner_is_first_player:
    print(f"Player two is out of eggs. Player one has {eggs_of_first_player} eggs left.")
elif winner_is_second_player:
    print(f"Player one is out of eggs. Player two has {eggs_of_second_player} eggs left.")
else:
    print(f"Player one has {eggs_of_first_player} eggs left.")
    print(f"Player two has {eggs_of_second_player} eggs left.")
