import math

hour_of_exam = int(input())
minute_of_exam = int(input())

hour_of_arrival = int(input())
minute_of_arrival = int(input())

hours_difference = hour_of_arrival - hour_of_exam
minute_difference = minute_of_arrival - minute_of_exam

total_minute_difference = minute_difference + hours_difference * 60

if 0 >= total_minute_difference >= -30:
    print('On time')
elif total_minute_difference > 0:
    print('Late')
elif total_minute_difference < -30:
    print('Early')

abs_total_minute_difference = abs(total_minute_difference)
if abs_total_minute_difference >= 1:
    if total_minute_difference >= 60:
        print(f'{math.floor(abs_total_minute_difference / 60):.0f}:{(abs_total_minute_difference % 60):02d} hours after the start')
    elif total_minute_difference <= -60:
        print(f'{math.floor(abs_total_minute_difference / 60):.0f}:{(abs_total_minute_difference % 60):02d} hours before the start')
    elif 1 <= total_minute_difference < 60:
        print(f'{abs_total_minute_difference} minutes after the start')
    elif -1 >= total_minute_difference > -60:
        print(f'{abs_total_minute_difference} minutes before the start')
