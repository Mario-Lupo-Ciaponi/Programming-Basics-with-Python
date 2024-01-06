a1 = int(input())
a2 = int(input())
n = int(input())

m = int(n / 2)

for first_symbol in range(a1, a2):
    for second_symbol in range(1, n):
        for third_symbol in range(1, m):
            forth_symbol = first_symbol

            if first_symbol % 2 != 0 and (second_symbol + third_symbol + forth_symbol) % 2 != 0:
                print(f"{chr(first_symbol)}-{second_symbol}{third_symbol}{forth_symbol}")
