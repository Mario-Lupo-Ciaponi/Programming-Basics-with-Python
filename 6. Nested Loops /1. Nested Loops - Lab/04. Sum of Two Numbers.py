import sys

start_of_interval = int(input())
end_of_interval = int(input())
magical_number = int(input())

count_of_combinations = 0

for i in range(start_of_interval, end_of_interval + 1):
    for y in range(start_of_interval, end_of_interval + 1):
        combination = i + y

        count_of_combinations += 1

        if combination == magical_number:
            print(f'Combination N:{count_of_combinations} ({i} + {y} = {magical_number})')
            sys.exit()

print(f'{count_of_combinations} combinations - neither equals {magical_number}')
