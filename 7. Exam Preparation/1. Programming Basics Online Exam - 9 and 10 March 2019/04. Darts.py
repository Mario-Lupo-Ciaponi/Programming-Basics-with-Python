import sys

name_of_player = input()
starter_points = 301

count_of_successful_shots = 0
count_of_unsuccessful_shots = 0

field = input()
while field != 'Retire':
    points = int(input())

    if field == 'Double':
        points = points * 2
    elif field == 'Triple':
        points = points * 3

    if points <= starter_points:
        count_of_successful_shots += 1
        starter_points -= points
    else:
        count_of_unsuccessful_shots += 1

    if starter_points == 0:
        print(f'{name_of_player} won the leg with {count_of_successful_shots} shots.')
        sys.exit()

    field = input()

print(f'{name_of_player} retired after {count_of_unsuccessful_shots} unsuccessful shots.')
