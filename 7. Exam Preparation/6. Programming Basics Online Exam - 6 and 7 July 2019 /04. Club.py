profit_wanted = float(input())

total_income = 0
profit_reached = False

name_of_cocktail = input()

while name_of_cocktail != "Party!":
    number_of_cocktails = int(input())

    income_of_cocktail = len(name_of_cocktail)

    current_income = number_of_cocktails * income_of_cocktail

    if current_income % 2 != 0:
        current_income -= current_income * 0.25

    total_income += current_income

    if total_income >= profit_wanted:
        profit_reached = True
        break

    name_of_cocktail = input()

if profit_reached:
    print("Target acquired.")
else:
    money_needed = profit_wanted - total_income
    print(f"We need {money_needed:.2f} leva more.")

print(f"Club income - {total_income:.2f} leva.")
