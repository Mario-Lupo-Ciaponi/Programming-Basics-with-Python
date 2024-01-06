hour = int(input())
day_of_the_week = input()
office_status = ''

if day_of_the_week == 'Monday' or day_of_the_week == 'Tuesday' or day_of_the_week == 'Wednesday' \
    or day_of_the_week == 'Thursday' or day_of_the_week == 'Friday' or day_of_the_week == 'Saturday':
    if hour >= 10 and hour <= 18:
        office_status = 'open'
    else:
        office_status = 'closed'
else:
    office_status = 'closed'

print(office_status)
