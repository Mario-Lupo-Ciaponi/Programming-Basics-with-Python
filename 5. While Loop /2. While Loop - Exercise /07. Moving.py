width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

command = input()

space_for_boxes = 0
no_free_space = False

while command != 'Done':
    space_for_boxes += int(command)

    if space_for_boxes > free_space:
        no_free_space = True
        break

    command = input()

if no_free_space:
    space_needed = space_for_boxes - free_space
    print(f'No more free space! You need {space_needed} Cubic meters more.')
else:
    space_left = free_space - space_for_boxes
    print(f'{space_left} Cubic meters left.')
