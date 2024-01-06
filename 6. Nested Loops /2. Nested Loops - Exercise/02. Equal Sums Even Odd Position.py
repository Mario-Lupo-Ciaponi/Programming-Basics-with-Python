start = int(input())
end = int(input())

for num in range(start, end + 1):
    num_in_str = str(num)

    even_sum = 0
    odd_sum = 0

    index = 0

    for element in num_in_str:


        if index % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)

        index += 1

    if even_sum == odd_sum:
        print(num, end=' ')
