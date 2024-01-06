command = input()

total_money = 0

while command != 'NoMoreMoney':
    money_deposited = float(command)

    if money_deposited < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {money_deposited:.2f}')
    total_money += money_deposited

    command = input()

print(f'Total: {total_money:.2f}')
