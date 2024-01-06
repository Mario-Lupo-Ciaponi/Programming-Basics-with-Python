import sys

money_needed_for_trip = float(input())
money_on_hand = float(input())

count_of_days = 0
streak_of_spending = 0

while money_on_hand < money_needed_for_trip:
    action = input()
    money_for_action = float(input())
    count_of_days += 1

    if action == 'save':
        money_on_hand += money_for_action
        streak_of_spending = 0
    else:
        money_on_hand -= money_for_action
        streak_of_spending += 1

    if streak_of_spending == 5:
        print('You can\'t save the money.')
        print(count_of_days)
        sys.exit()

    if money_on_hand < 0:
        money_on_hand = 0

print(f'You saved the money for {count_of_days} days.')
