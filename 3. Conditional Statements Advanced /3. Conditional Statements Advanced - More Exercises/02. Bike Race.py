count_of_junior_bikers = int(input())
count_of_senior_bikers = int(input())
type_of_trace = input()

money_for_charity = 0

count_of_all_bikers = count_of_junior_bikers + count_of_senior_bikers

if type_of_trace == 'trail':
    money_for_charity = count_of_junior_bikers * 5.5 + count_of_senior_bikers * 7
elif type_of_trace == 'cross-country':
    money_for_charity = count_of_junior_bikers * 8 + count_of_senior_bikers * 9.5

    if count_of_all_bikers >= 50:
        money_for_charity -= money_for_charity * 0.25
elif type_of_trace == 'downhill':
    money_for_charity = count_of_junior_bikers * 12.25 + count_of_senior_bikers * 13.75
else:
    money_for_charity = count_of_junior_bikers * 20 + count_of_senior_bikers * 21.5

money_for_charity -= money_for_charity * 0.05

print(f'{money_for_charity:.2f}')
