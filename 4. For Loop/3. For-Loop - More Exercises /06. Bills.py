months = int(input())

electricity_total_price = 0
water_total_price = 0
internet_total_price = 0
other_total_price = 0

for i in range(months):
    electricity_price = float(input())

    electricity_total_price += electricity_price
    water_total_price += 20
    internet_total_price += 15
    other_total_price += (electricity_price + 20 + 15) * 1.2

average = (electricity_total_price + water_total_price + internet_total_price + other_total_price) / months

print(f'Electricity: {electricity_total_price:.2f} lv')
print(f'Water: {water_total_price:.2f} lv')
print(f'Internet: {internet_total_price:.2f} lv')
print(f'Other: {other_total_price:.2f} lv')
print(f'Average: {average:.2f} lv')
