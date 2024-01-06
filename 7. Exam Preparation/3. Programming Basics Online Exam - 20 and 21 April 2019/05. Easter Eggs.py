import sys

count_of_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for i in range(count_of_eggs):
    color = input()

    if color == "red":
        red_eggs += 1
    elif color == "orange":
        orange_eggs += 1
    elif color == "blue":
        blue_eggs += 1
    else:
        green_eggs += 1

most_colored_eggs = max(red_eggs, orange_eggs, blue_eggs, green_eggs)
most_used_color = ""

if red_eggs > orange_eggs and red_eggs > blue_eggs  and red_eggs > green_eggs:
    most_used_color = "red"
elif orange_eggs > red_eggs and orange_eggs > blue_eggs  and orange_eggs > green_eggs:
    most_used_color = "orange"
elif blue_eggs > red_eggs and blue_eggs > orange_eggs  and blue_eggs > green_eggs:
    most_used_color = "blue"
else:
    most_used_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {most_colored_eggs} -> {most_used_color}")
