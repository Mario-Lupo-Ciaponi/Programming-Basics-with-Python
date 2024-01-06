import math

count_of_tournaments = int(input())
points = int(input())

points_won = 0
tournaments_won = 0

for i in range(count_of_tournaments):
    tournament_stage_reached = input()

    if tournament_stage_reached == 'W':
        points_won += 2000
        tournaments_won += 1
    elif tournament_stage_reached == 'F':
        points_won += 1200
    else:
        points_won += 720

total_points = points + points_won

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(points_won / count_of_tournaments)}')
print(f'{(tournaments_won / count_of_tournaments * 100):.2f}%')
