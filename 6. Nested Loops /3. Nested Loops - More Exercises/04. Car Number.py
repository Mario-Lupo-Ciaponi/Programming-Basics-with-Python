start = int(input())
end = int(input())

secret_code_is_good = False

for first_num in range(start, end + 1):
    for second_num in range(start, end + 1):
        for third_num in range(start, end + 1):
            for fourth_num in range(start, end + 1):
                if first_num % 2 == 0 and fourth_num % 2 != 0 and first_num > fourth_num and (
                        second_num + third_num) % 2 == 0:
                    secret_code_is_good = True
                if first_num % 2 != 0 and fourth_num % 2 == 0 and first_num > fourth_num and (
                        second_num + third_num) % 2 == 0:
                    secret_code_is_good = True

                if secret_code_is_good:
                    print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
                    secret_code_is_good = False
