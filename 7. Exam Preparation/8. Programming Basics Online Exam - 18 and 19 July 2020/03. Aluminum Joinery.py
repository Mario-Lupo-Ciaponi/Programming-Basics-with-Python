import sys

count_of_windows = int(input())
type_of_windows = input()
delivery = input()

price_per_window = 0

if count_of_windows < 10:
    print("Invalid order")
    sys.exit()

if type_of_windows == "90X130":
    price_per_window = 110

    if 30 < count_of_windows <= 60:
        price_per_window -= price_per_window * 0.05
    elif count_of_windows > 60:
        price_per_window -= price_per_window * 0.08
elif type_of_windows == "100X150":
    price_per_window = 140

    if 40 < count_of_windows <= 80:
        price_per_window -= price_per_window * 0.06
    elif count_of_windows > 80:
        price_per_window -= price_per_window * 0.1
elif type_of_windows == "130X180":
    price_per_window = 190

    if 20 < count_of_windows <= 50:
        price_per_window -= price_per_window * 0.07
    elif count_of_windows > 50:
        price_per_window -= price_per_window * 0.12
else:
    price_per_window = 250

    if 25 < count_of_windows <= 50:
        price_per_window -= price_per_window * 0.09
    elif count_of_windows > 50:
        price_per_window -= price_per_window * 0.14

price_of_windows = count_of_windows * price_per_window

if delivery == "With delivery":
    price_of_windows += 60

if count_of_windows > 99:
    price_of_windows -= price_of_windows * 0.04

print(f"{price_of_windows:.2f} BGN")
