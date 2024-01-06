name_of_first_player = input()
name_of_second_player = input()

command = input()

first_player_points = 0
second_player_points = 0

number_war = False
number_war_winner = ''
number_war_points = 0

while command != 'End of game':
    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        second_player_points += second_player_card - first_player_card
    else:
        number_war = True

        first_player_card = int(input())
        second_player_card = int(input())

        if first_player_card > second_player_card:
            number_war_winner = name_of_first_player
            number_war_points = first_player_points
        else:
            number_war_winner = name_of_second_player
            number_war_points = second_player_points

        break

    command = input()

if number_war:
    print('Number wars!')
    print(f'{number_war_winner} is winner with {number_war_points} points')
else:
    print(f'{name_of_first_player} has {first_player_points} points')
    print(f'{name_of_second_player} has {second_player_points} points')
