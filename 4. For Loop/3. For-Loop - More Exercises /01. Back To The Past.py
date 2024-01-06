money_inherited = float(input())
years_to_live =int(input())
ivan_years = 18

money_for_spending = 0

for i in range(1800, years_to_live+ 1):
    if i % 2 == 0:
        money_for_spending += 12000
    else:
        money_for_spending += 12000 + 50 * ivan_years

    ivan_years += 1

if money_inherited >= money_for_spending:
    money_left = money_inherited - money_for_spending
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
    money_needed = money_for_spending - money_inherited
    print(f'He will need {money_needed:.2F} dollars to survive.')
