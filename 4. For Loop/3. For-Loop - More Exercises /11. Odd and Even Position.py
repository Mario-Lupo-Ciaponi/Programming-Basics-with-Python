import sys

n = int(input())

count_odd = 0
count_even = 0

odd_sum = 0
even_sum = 0

odd_min = sys.maxsize
even_min = sys.maxsize

odd_max = -sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 0:
        even_sum += number
        count_even += 1

        if number > even_max:
            even_max = number

        if number < even_min:
            even_min = number
    else:
        odd_sum += number
        count_odd += 1

        if number > odd_max:
            odd_max = number

        if number < odd_min:
            odd_min = number

if count_even == 0:
    even_max = 'No'
    even_min = 'No'
else:
    even_max = f'{even_max:.2f}'
    even_min = f'{even_min:.2f}'

if count_odd == 0:
    odd_max = 'No'
    odd_min = 'No'
else:
    odd_max = f'{odd_max:.2f}'
    odd_min = f'{odd_min:.2f}'

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={odd_min},')
print(f'OddMax={odd_max},')
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={even_min},')
print(f'EvenMax={even_max}')
