count_of_loads = int(input())

price_of_tons = 0

microbus_load_count = 0
truck_load_count = 0
train_load_count = 0

count_of_tons = 0

for i in range(count_of_loads):
    tons_of_load = int(input())

    if tons_of_load <= 3:
        microbus_load_count += tons_of_load
        price_of_tons += tons_of_load * 200
    elif 4 <= tons_of_load <= 11:
        truck_load_count += tons_of_load
        price_of_tons += tons_of_load * 175
    else:
        train_load_count += tons_of_load
        price_of_tons += tons_of_load * 120

    count_of_tons += tons_of_load

print(f'{(price_of_tons / count_of_tons):.2f}')
print(f'{(microbus_load_count  / count_of_tons * 100):.2f}%')
print(f'{(truck_load_count / count_of_tons * 100):.2f}%')
print(f'{(train_load_count / count_of_tons * 100):.2f}%')
