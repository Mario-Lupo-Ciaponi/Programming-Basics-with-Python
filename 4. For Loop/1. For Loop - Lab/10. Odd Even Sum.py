count_of_times = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, count_of_times + 1):
    number = int(input())

    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    difference = abs(even_sum - odd_sum)

    print('No')
    print(f'Diff = {difference}')
