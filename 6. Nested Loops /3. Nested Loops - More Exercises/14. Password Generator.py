letter = int(input())

another_num = 2

for i in range(1, number):
    for j in range(1, number):
        for k in range(1, letter + 1):
            for l in range(1, letter + 1):
                for m in range(max(i, j) + 1, number + 1):
                    print(f"{i}{j}{chr(ord('`') + k)}{chr(ord('`') + l)}{m}", end=" ")
