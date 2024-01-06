season = input()
type_of_group = input()
number_of_students = int(input())
count_of_nights = int(input())

sport = ''
price = 0
price_for_one_person = 0

if season == 'Winter':
    if type_of_group == 'boys' or type_of_group == 'girls':
        sport = "Gymnastics" if type_of_group == 'girls' else "Judo"
        price_for_one_person = 9.6
    else:
        sport = 'Ski'
        price_for_one_person = 10


elif season == 'Spring':
    if type_of_group == 'boys' or type_of_group == 'girls':
        sport = "Athletics" if type_of_group == 'girls' else "Tennis"
        price_for_one_person = 7.2
    else:
        sport = 'Cycling'
        price_for_one_person = 9.5

else:
    if type_of_group == 'boys' or type_of_group == 'girls':
        sport = "Volleyball" if type_of_group == 'girls' else "Football"
        price_for_one_person = 15
    else:
        sport = 'Swimming'
        price_for_one_person = 20

price = price_for_one_person * number_of_students * count_of_nights

if 10 <= number_of_students < 20:
    price *= 0.95
elif 20 <= number_of_students < 50:
    price *= 0.85
elif number_of_students >= 50:
    price /= 2

print(f'{sport} {price:.2f} lv.')
