day_of_the_week = int(input())
name_of_the_day = ''

if day_of_the_week == 1:
    name_of_the_day = 'Monday'
elif day_of_the_week == 2:
    name_of_the_day = 'Tuesday'
elif day_of_the_week == 3:
    name_of_the_day = 'Wednesday'
elif day_of_the_week == 4:
    name_of_the_day = 'Thursday'
elif day_of_the_week == 5:
    name_of_the_day = 'Friday'
elif day_of_the_week == 6:
    name_of_the_day = 'Saturday'
elif day_of_the_week == 7:
    name_of_the_day = 'Sunday'
else:
    name_of_the_day = 'Error'

print(name_of_the_day)
