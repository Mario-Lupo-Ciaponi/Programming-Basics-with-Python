name = input()
grade = 1

time_excluded = 0

average_grade = 0

while grade <= 12:
    if time_excluded == 2:
        print(f'{name} has been excluded at {grade} grade')
        break

    year_grade = float(input())

    if year_grade < 4:
        time_excluded += 1
        continue

    average_grade += year_grade
    grade += 1

if time_excluded < 2:
    print(f'{name} graduated. Average grade: {(average_grade / 12):.2f}')
