number_to_reach = int(input())

counter = 1

for row in range(1, number_to_reach + 1):
    for cow in range(1, row + 1):
        print(counter, end=' ')
        counter += 1

        if counter > number_to_reach:
            break

    if counter > number_to_reach:
        break

    print()
    