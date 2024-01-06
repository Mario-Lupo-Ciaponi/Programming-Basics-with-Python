width = int(input())
length = int(input())

size_of_cake = width * length

no_more_cake = False

command = input()

while command != 'STOP':
    size_of_cake -= int(command)

    if size_of_cake < 0:
        no_more_cake = True
        break

    command = input()

if no_more_cake:
    print(f'No more cake left! You need {abs(size_of_cake)} pieces more.')
else:
    print(f'{size_of_cake} pieces are left.')
