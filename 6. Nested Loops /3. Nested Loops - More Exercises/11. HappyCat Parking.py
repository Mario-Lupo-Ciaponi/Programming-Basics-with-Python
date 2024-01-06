count_of_days = int(input())
count_of_hours_per_day = int(input())

total_tax = 0

for day in range(1, count_of_days + 1):
    tax = 0
    for hour in range(1, count_of_hours_per_day + 1):
        if day % 2 == 0:
            if hour % 2 != 0:
                tax += 2.5
                total_tax += 2.5
            else:
                tax += 1
                total_tax += 1
        else:
            if hour % 2 == 0:
                tax += 1.25
                total_tax += 1.25
            else:
                tax += 1
                total_tax += 1

    print(f"Day: {day} - {tax:.2f} leva")

print(f"Total: {total_tax:.2f} leva")
