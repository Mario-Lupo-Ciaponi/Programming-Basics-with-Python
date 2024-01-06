season = input()
kilometers_per_month = float(input())

month_salary = 0

if kilometers_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        month_salary = kilometers_per_month * 0.75
    elif season == 'Summer':
        month_salary = kilometers_per_month * 0.9
    else:
        month_salary = kilometers_per_month * 1.05
elif 5000 <= kilometers_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        month_salary = kilometers_per_month * 0.95
    elif season == 'Summer':
        month_salary = kilometers_per_month * 1.1
    else:
        month_salary = kilometers_per_month * 1.25
elif 10000 < kilometers_per_month <= 20000:
    month_salary = kilometers_per_month * 1.45

season_salary = month_salary * 4
season_salary -= season_salary * 0.1

print(f'{season_salary:.2f}')
