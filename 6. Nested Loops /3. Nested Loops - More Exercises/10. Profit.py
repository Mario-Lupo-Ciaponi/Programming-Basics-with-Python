count_one_levas = int(input())
count_two_levas = int(input())
count_five_levas = int(input())
sum = int(input())

for i in range(0, count_one_levas + 1):
    for j in range(0, count_two_levas + 1):
        for k in range(0, count_five_levas + 1):
            if i * 1 + j * 2 + k * 5 == sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sum} lv.")
