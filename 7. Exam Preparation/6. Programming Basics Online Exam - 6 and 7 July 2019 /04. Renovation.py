import math

height_of_wall = int(input())
width_of_wall = int(input())
percent_not_for_coloring = int(input())

area_of_wall = height_of_wall * width_of_wall
area_of_four_walls = area_of_wall * 4

total_area = math.ceil(area_of_four_walls - area_of_four_walls * (percent_not_for_coloring / 100))

room_painted = False

command = input()

while command != "Tired!":
    total_area -= int(command)

    if total_area <= 0:
        room_painted = True
        break

    command = input()

if room_painted:
    if total_area == 0:
        print("All walls are painted! Great job, Pesho!")
    else:
        print(f"All walls are painted and you have {abs(total_area)} l paint left!")
else:
    print(f"{total_area} quadratic m left.")
