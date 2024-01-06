type_of_fuel = input()
liters = float(input())

if type_of_fuel == 'Gas' or type_of_fuel == 'Diesel' or type_of_fuel == 'Gasoline':
    if liters >= 25:
        print(f'You have enough {type_of_fuel.lower()}.')
    else:
        print(f'Fill your tank with {type_of_fuel.lower()}!')
else:
    print('Invalid fuel!')
