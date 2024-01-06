capacity_of_stadium = int(input())
count_of_fans = int(input())

a_count = 0
b_count = 0
v_count = 0
g_count = 0

for i in range(count_of_fans):
    sector = input()

    if  sector == 'A':
        a_count += 1
    elif sector == 'B':
        b_count += 1
    elif sector == 'V':
        v_count += 1
    else:
        g_count += 1

print(f'{(a_count / count_of_fans * 100):.2f}%')
print(f'{(b_count / count_of_fans * 100):.2f}%')
print(f'{(v_count / count_of_fans * 100):.2f}%')
print(f'{(g_count / count_of_fans * 100):.2f}%')
print(f'{(count_of_fans / capacity_of_stadium * 100):.2f}%')
