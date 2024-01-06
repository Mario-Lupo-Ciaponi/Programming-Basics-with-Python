destination = input()

saved_money = 0

while destination != 'End':
    money_needed = float(input())

    while saved_money <= money_needed:
        saved_money += float(input())

        if saved_money >= money_needed:
            print(f'Going to {destination}!')
            break

    destination = input()
    saved_money = 0
