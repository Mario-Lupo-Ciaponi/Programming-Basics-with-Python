norm_of_tom = 30000

count_of_holidays = int(input())
count_of_working_days = 365 - count_of_holidays

holiday_playing_hours = count_of_holidays * 127
working_playing_hours = count_of_working_days * 63

total_hour_playing = holiday_playing_hours + working_playing_hours

if norm_of_tom >= total_hour_playing:
    less_plays_minutes = norm_of_tom - total_hour_playing

    hours_less_playing = less_plays_minutes // 60
    minutes_less_playing = less_plays_minutes % 60

    print(f'Tom sleeps well')
    print(f'{hours_less_playing} hours and {minutes_less_playing} minutes less for play')
else:
    more_playing_minutes = total_hour_playing - norm_of_tom

    print('Tom will run away')
    print(f'{more_playing_minutes // 60} hours and {more_playing_minutes % 60} minutes more for play')
