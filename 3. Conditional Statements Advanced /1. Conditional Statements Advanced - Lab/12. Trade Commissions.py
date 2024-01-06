town = input()
sales_volume = float(input())
commission = 0
valid = True

if town == 'Sofia':
    if sales_volume >= 0 and sales_volume <= 500:
        commission = sales_volume * 0.05
    elif sales_volume > 500 and sales_volume <= 1000:
        commission = sales_volume * 0.07
    elif sales_volume > 1000 and sales_volume <= 10000:
        commission = sales_volume * 0.08
    elif sales_volume > 10000:
        commission = sales_volume * 0.12
    else:
        valid = False
elif town == 'Varna':
    if sales_volume >= 0 and sales_volume <= 500:
        commission = sales_volume * 0.045
    elif sales_volume > 500 and sales_volume <= 1000:
        commission = sales_volume * 0.075
    elif sales_volume > 1000 and sales_volume <= 10000:
        commission = sales_volume * 0.1
    elif sales_volume > 10000:
        commission = sales_volume * 0.13
    else:
        valid = False
elif town == 'Plovdiv':
    if sales_volume >= 0 and sales_volume <= 500:
        commission = sales_volume * 0.055
    elif sales_volume > 500 and sales_volume <= 1000:
        commission = sales_volume * 0.08
    elif sales_volume > 1000 and sales_volume <= 10000:
        commission = sales_volume * 0.12
    elif sales_volume > 10000:
        commission = sales_volume * 0.145
    else:
        valid = False
else:
    valid = False

if valid:
    print(f'{commission:.2f}')
else:
    print('error')
