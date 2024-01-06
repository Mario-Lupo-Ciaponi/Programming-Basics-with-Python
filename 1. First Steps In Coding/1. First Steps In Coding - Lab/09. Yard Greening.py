qubic_meters_of_yard = float(input())

price_without_discount = qubic_meters_of_yard * 7.61
discount = price_without_discount * 0.18
price_with_discount = price_without_discount - discount

print(f'The final price is: {price_with_discount} lv.')
print(f'The discount is: {discount} lv.')
