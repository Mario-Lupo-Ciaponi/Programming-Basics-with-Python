import math

figure = input()
a = float(input())
area = 0

if figure == 'square':
    area = a * a
elif figure == 'rectangle':
    b = float(input())
    area = a * b
elif figure == 'triangle':
    h = float(input())
    area = (a * h) / 2
else:
    r = a
    area = math.pi * (r ** 2)

print(f'{area:.3f}')
