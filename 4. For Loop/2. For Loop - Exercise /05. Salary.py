count_of_tabs = int(input())
salary = int(input())

for tab in range(0, count_of_tabs):
    website = input()

    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50

if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')
