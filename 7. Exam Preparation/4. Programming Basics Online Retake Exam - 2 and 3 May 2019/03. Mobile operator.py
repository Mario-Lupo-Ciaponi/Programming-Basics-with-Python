duration_of_contract = input()
type_of_contract = input()
add_mobile_internet = input()
months_of_payment = int(input())

tax = 0

if duration_of_contract == "one":
    if type_of_contract == "Small":
        tax = 9.98
    elif type_of_contract == "Middle":
        tax = 18.99
    elif type_of_contract == "Large":
        tax = 25.98
    else:
        tax = 35.99
else:
    if type_of_contract == "Small":
        tax = 8.58
    elif type_of_contract == "Middle":
        tax = 17.09
    elif type_of_contract == "Large":
        tax = 23.59
    else:
        tax = 31.79

if add_mobile_internet == "yes":
    if tax <= 10:
        tax += 5.5
    elif 10 < tax <= 30:
        tax += 4.35
    else:
        tax += 3.85

if duration_of_contract == "two":
    tax -= tax * 0.0375

total_tax = tax * months_of_payment

print(f"{total_tax:.2f} lv.")
