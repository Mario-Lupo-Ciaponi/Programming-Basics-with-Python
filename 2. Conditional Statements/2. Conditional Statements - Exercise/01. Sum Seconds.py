time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_of_second = time_first + time_second + time_third

time_minutes = sum_of_second // 60
time_seconds = sum_of_second % 60\

if time_seconds < 10:
    print(f'{time_minutes}:0{time_seconds}')
else:
    print(f'{time_minutes}:{time_seconds}')
