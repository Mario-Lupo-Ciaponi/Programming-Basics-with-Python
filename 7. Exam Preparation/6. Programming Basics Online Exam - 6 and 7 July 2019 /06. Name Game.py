import sys

best_player = ""
best_points = -sys.maxsize

name = input()
while name != "Stop":
    points = 0

    for letter in name:
        number = int(input())

        if number == ord(letter):
            points += 10
        else:
            points += 2

    if points >= best_points:
        best_player = name
        best_points = points

    name = input()

print(f"The winner is {best_player} with {best_points} points!")
