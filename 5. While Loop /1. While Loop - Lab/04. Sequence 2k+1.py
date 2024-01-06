n = int(input())

last_number = 0
current_num = 0

while True:
    current_num = last_number * 2 + 1

    if current_num <= n:
        print(current_num)
    else:
        break

    last_number = current_num
