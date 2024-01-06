import math

series_name = input()
duration_of_episode = int(input())
duration_of_break = int(input())

lunch_break = duration_of_break / 8
rest_time = duration_of_break / 4

total_time_needed = duration_of_episode + lunch_break + rest_time

if duration_of_break >= total_time_needed:
    time_left = duration_of_break - total_time_needed
    print(f'You have enough time to watch {series_name} and left with {math.ceil(time_left)} minutes free time.')
else:
    missing_time = total_time_needed - duration_of_break
    print(f'You don\'t have enough time to watch {series_name}, you need {math.ceil(missing_time)} more minutes.')
