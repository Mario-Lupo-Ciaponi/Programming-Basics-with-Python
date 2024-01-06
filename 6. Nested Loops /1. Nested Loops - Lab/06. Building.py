floors = int(input())
rooms = int(input())

number_of_room = floors * 10
type_of_room = ''
last_floor = True

floor_look = ''

for floor in range(floors, 0, -1):

    current_room = number_of_room
    for room in range(1, rooms + 1):


        if last_floor:
            type_of_room = 'L'
        elif floor % 2 == 0:
            type_of_room = 'O'
        else:
            type_of_room = 'A'

        floor_look += f'{type_of_room}{current_room} '
        current_room += 1

    print(floor_look)
    floor_look = ''

    last_floor = False
    number_of_room -= 10
