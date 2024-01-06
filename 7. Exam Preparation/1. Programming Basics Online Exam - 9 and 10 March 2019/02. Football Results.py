first_mach_results = input()
second_mach_results = input()
third_mach_results = input()

games_won = 0
games_lost = 0
games_drawn = 0

if int(first_mach_results[0]) > int(first_mach_results[2]):
    games_won += 1
elif int(first_mach_results[0]) < int(first_mach_results[2]):
    games_lost += 1
else:
    games_drawn += 1

if int(second_mach_results[0]) > int(second_mach_results[2]):
    games_won += 1
elif int(second_mach_results[0]) < int(second_mach_results[2]):
    games_lost += 1
else:
    games_drawn += 1

if int(third_mach_results[0]) > int(third_mach_results[2]):
    games_won += 1
elif int(third_mach_results[0]) < int(third_mach_results[2]):
    games_lost += 1
else:
    games_drawn += 1

print(f'Team won {games_won} games.')
print(f'Team lost {games_lost} games.')
print(f'Drawn games: {games_drawn}')
