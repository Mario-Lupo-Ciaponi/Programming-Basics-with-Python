type_of_fuel = input()
liters_of_fuel = float(input())
club_card = input()

gasoline_price_per_liter = 2.22
diesel_price_per_liter = 2.33
gas_price_per_liter = 0.93

fuel_total_price = 0

if club_card == 'Yes':
    gasoline_price_per_liter -= 0.18
    diesel_price_per_liter -= 0.12
    gas_price_per_liter -= 0.08

if type_of_fuel == 'Gasoline':
    fuel_total_price = liters_of_fuel * gasoline_price_per_liter
elif type_of_fuel == 'Diesel':
    fuel_total_price = liters_of_fuel * diesel_price_per_liter
else:
    fuel_total_price = liters_of_fuel * gas_price_per_liter

if 20 <= liters_of_fuel <= 25:
    fuel_total_price -= fuel_total_price * 0.08
elif liters_of_fuel > 25:
    fuel_total_price -= fuel_total_price * 0.1

print(f'{fuel_total_price:.2f} lv.')
