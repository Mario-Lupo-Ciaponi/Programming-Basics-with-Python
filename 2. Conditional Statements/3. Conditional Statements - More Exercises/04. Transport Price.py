kilometers = int(input())
time_of_the_day = input()
price = 0

if kilometers < 20:
    price = 0.7

    if time_of_the_day == 'day':
        price += kilometers * 0.79
    else:
        price += kilometers * 0.9
elif 20 <= kilometers < 100:
    price = kilometers * 0.09
else:
    price = kilometers * 0.06

print(f'{price:.2f}')
