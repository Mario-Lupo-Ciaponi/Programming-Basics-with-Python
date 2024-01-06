import sys

number_of_times = int(input())

max_num = -sys.maxsize
sum = 0

for i in range(0, number_of_times):
    number = int(input())

    if max_num < number:
        max_num = number

    sum += number

sum -= max_num

if sum == max_num:
    print('Yes')
    print(f'Sum = {sum}')
else:
    difference = abs(sum - max_num)

    print('No')
    print(f'Diff = {difference}')
