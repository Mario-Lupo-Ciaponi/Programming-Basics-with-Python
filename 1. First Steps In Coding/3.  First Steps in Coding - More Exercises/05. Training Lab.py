import math

w = float(input())
h = float(input())

rows = math.floor(((h * 100) - 100) / 70)
places = math.floor(w * 100 / 120)
work_places = rows * places - 3

print(work_places)
