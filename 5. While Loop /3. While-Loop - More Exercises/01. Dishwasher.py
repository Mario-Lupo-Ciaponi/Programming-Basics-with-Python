import sys

count_of_dish_detergent = int(input())

ml_of_detergent = count_of_dish_detergent * 750

i = 1
ml_needed = 0

number_of_dishes = 0
number_of_pots = 0

command = input()
while command != 'End':
    bottle_count = int(command)

    if i % 3 == 0:
        ml_needed += bottle_count * 15

        number_of_pots += bottle_count
    else:
        ml_needed += bottle_count * 5

        number_of_dishes += bottle_count

    if ml_needed > ml_of_detergent:
        print(f'Not enough detergent, {ml_needed - ml_of_detergent} ml. more necessary!')
        sys.exit()

    command = input()
    i += 1

print('Detergent was enough!')
print(f'{number_of_dishes} dishes and {number_of_pots} pots were washed.')
print(f'Leftover detergent {ml_of_detergent - ml_needed} ml.')
