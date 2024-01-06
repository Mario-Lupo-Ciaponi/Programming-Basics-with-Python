count_of_men = int(input())
count_of_women = int(input())
count_of_tables = int(input())

counter = 0
couples = ''

for i in range(1, count_of_men + 1):
    for j in range(1, count_of_women + 1):
        counter += 1
        couples += f'({i} <-> {j}) '

        if counter == count_of_tables:
            break

    if counter == count_of_tables:
        break

print(couples)
