starter_value_of_first_pair = int(input())
starter_value_of_second_pair = int(input())
difference_of_first_pair = int(input())
difference_of_second_pair = int(input())

starter_value = starter_value_of_first_pair + difference_of_first_pair
final_value = starter_value_of_second_pair + difference_of_second_pair

first_counter = 0
second_counter = 0

for i in range(starter_value_of_first_pair, starter_value + 1):
    first_counter = 0

    for k in range(1, i + 1):
        if i % k == 0:
            first_counter += 1

    if first_counter == 2:
        for j in range(starter_value_of_second_pair, final_value + 1):
            second_counter = 0

            for l in range(1, j + 1):
                if j % l == 0:
                    second_counter += 1

            if second_counter == 2:
                print(f"{i}{j}")
