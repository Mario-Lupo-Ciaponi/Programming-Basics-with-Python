import sys

money_needed_for_charity = int(input())

money_collected = 0

cash_money = 0
credit_card_money = 0

cash_count = 0
credit_card_count = 0

i = 0

command = input()
while command != 'End':
    money_for_transaction= int(command)

    if i % 2 == 0:
        if money_for_transaction > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')

            money_collected += money_for_transaction
            cash_money += money_for_transaction
            cash_count += 1

    else:
        if money_for_transaction < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')

            money_collected += money_for_transaction
            credit_card_money += money_for_transaction
            credit_card_count += 1

    if money_collected >= money_needed_for_charity:
        print(f'Average CS: {(cash_money / cash_count):.2f}')
        print(f'Average CC: {(credit_card_money / credit_card_count):.2f}')
        sys.exit()

    command = input()
    i += 1

print('Failed to collect required money for charity.')
