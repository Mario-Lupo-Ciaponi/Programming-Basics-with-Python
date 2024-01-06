import sys

budget = float(input())

name = input()

while name != "ACTION":
    if len(name) > 15:
        budget -= budget * 0.2
    else:
        budget -= float(input())

    if budget < 0:
        budget = abs(budget)

        print(f"We need {budget:.2f} leva for our actors.")
        sys.exit()

    name = input()

print(f"We are left with {budget:.2f} leva.")
