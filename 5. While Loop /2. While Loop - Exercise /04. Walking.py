goal = 10000

command = input()
total_steps = 0

while command != 'Going home':
    total_steps += int(command)

    if total_steps >= goal:
        break

    command = input()

if command == 'Going home':
    total_steps += int(input())

if total_steps >= goal:
    print('Goal reached! Good job!')
    print(f'{total_steps - goal} steps over the goal!')
else:
    print(f'{goal - total_steps} more steps to reach goal.')
