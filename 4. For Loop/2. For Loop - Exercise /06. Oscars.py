actor_name = input()
academy_points = float(input())
judges_count = int(input())

points_needed = 1250.5

for i in range(judges_count):
    if academy_points >= points_needed:
        break

    judge_name = input()
    points_given = float(input())

    academy_points += (points_given * len(judge_name)) / 2

if academy_points >= points_needed:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {(points_needed - academy_points):.1f} more!')
