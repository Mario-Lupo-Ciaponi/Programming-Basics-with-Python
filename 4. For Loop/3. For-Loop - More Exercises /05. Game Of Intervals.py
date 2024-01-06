count_of_intervals = int(input())
result = 0

first_interval_count = 0
second_interval_count = 0
third_interval_count = 0
fourth_interval_count = 0
fifth_interval_count = 0

invalid_interval_count = 0

for i in range(count_of_intervals):
    interval = int(input())

    if 0 <= interval <= 9:
        result += interval * 0.2
        first_interval_count += 1
    elif 10 <= interval <= 19:
        result += interval * 0.3
        second_interval_count += 1
    elif 20 <= interval <= 29:
        result += interval * 0.4
        third_interval_count += 1
    elif 30 <= interval <= 39:
        result += 50
        fourth_interval_count += 1
    elif 40 <= interval <= 50:
        result += 100
        fifth_interval_count += 1
    else:
        result /= 2
        invalid_interval_count += 1

first_interval_percent = first_interval_count / count_of_intervals * 100
second_interval_percent = second_interval_count / count_of_intervals * 100
third_interval_percent = third_interval_count / count_of_intervals * 100
fourth_interval_percent = fourth_interval_count / count_of_intervals * 100
fifth_interval_percent = fifth_interval_count / count_of_intervals * 100

invalid_interval_percent = invalid_interval_count / count_of_intervals * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {first_interval_percent:.2f}%')
print(f'From 10 to 19: {second_interval_percent:.2f}%')
print(f'From 20 to 29: {third_interval_percent:.2f}%')
print(f'From 30 to 39: {fourth_interval_percent:.2f}%')
print(f'From 40 to 50: {fifth_interval_percent:.2f}%')
print(f'Invalid numbers: {invalid_interval_percent:.2f}%')
