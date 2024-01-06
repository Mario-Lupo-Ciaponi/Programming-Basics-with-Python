type_of_projection = input()
rows = int(input())
columns = int(input())

total_places = rows * columns
price = 0

if type_of_projection == 'Premiere':
    price = 12
elif type_of_projection == 'Normal':
    price = 7.5
elif type_of_projection == 'Discount':
    price = 5

total_price = total_places * price

print(f'{total_price:.2f} leva')
