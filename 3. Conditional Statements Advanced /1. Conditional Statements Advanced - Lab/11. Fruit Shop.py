fruit = input()
day_of_the_week = input()
quantity = float(input())
price = 0
valid = True

if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' \
    or day_of_the_week == 'Thursday' or day_of_the_week == 'Friday':
    if fruit == 'banana':
        price = quantity * 2.5
    elif fruit == 'apple':
        price = quantity * 1.2
    elif fruit == 'orange':
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == 'kiwi':
        price = quantity * 2.7
    elif fruit == 'pineapple':
        price = quantity * 5.5
    elif fruit == 'grapes':
        price = quantity * 3.85
    else:
        valid = False
elif day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
    if fruit == 'banana':
        price = quantity * 2.7
    elif fruit == 'apple':
        price = quantity * 1.25
    elif fruit == 'orange':
        price = quantity * 0.9
    elif fruit == 'grapefruit':
        price = quantity * 1.6
    elif fruit == 'kiwi':
        price = quantity * 3
    elif fruit == 'pineapple':
        price = quantity * 5.6
    elif fruit == 'grapes':
        price = quantity * 4.2
    else:
        valid = False
else:
    valid = False

if valid:
    print(f'{price:.2f}')
else:
    print('error')