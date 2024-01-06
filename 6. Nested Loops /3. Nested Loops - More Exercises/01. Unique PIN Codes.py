upper_border_of_first_digit = int(input())
upper_border_of_second_digit = int(input())
upper_border_of_third_digit = int(input())

for i in range(1, upper_border_of_first_digit + 1):
    for j in range(1, upper_border_of_second_digit + 1):
        for h in range(1, upper_border_of_third_digit + 1):
            code = ""

            if i % 2 == 0:
                code += f"{str(i)} "
            if j == 2 or j == 3 or j == 5 or j == 7:
                code += f"{str(j)} "
            if h % 2 == 0:
                code += f"{str(h)}"

            if len(code) == 5:
                print(code)
