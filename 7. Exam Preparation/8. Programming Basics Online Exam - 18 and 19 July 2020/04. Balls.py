import math

count_of_balls = int(input())

points = 0

red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0

for i in range(count_of_balls):
    color_of_ball = input()

    if color_of_ball == "red":
        points += 5
        red_balls += 1
    elif color_of_ball == "orange":
        points += 10
        orange_balls += 1
    elif color_of_ball == "yellow":
        points += 15
        yellow_balls += 1
    elif color_of_ball == "white":
        points += 20
        white_balls += 1
    elif color_of_ball == "black":
        points = math.floor(points / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
