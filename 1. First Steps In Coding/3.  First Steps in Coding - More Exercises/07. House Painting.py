x = float(input())
y = float(input())
h = float(input())

door_area = 1.2 * 2
windows_area = 1.5 * 1.5

small_walls = x * x
side_walls = x * y

qubic_meters_of_walls = (small_walls * 2) + (side_walls * 2)
qubic_meters_of_with_door = qubic_meters_of_walls - (door_area + (windows_area * 2))

liters_of_green_paint = qubic_meters_of_with_door / 3.4

front_and_back_roof = (x * h) / 2
side_roof = x * y

qubic_meters = (front_and_back_roof * 2) + (side_roof * 2)

liters_of_red_paint = qubic_meters / 4.3

print(f'{liters_of_green_paint:.2f}')
print(f'{liters_of_red_paint:.2f}')
