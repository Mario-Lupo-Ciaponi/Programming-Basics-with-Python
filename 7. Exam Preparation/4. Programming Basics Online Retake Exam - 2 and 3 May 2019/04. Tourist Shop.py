budget = float(input())


product = input()
not_enough_money = False
number_of_product = 1

total_price = 0

while product != "Stop":
    price_of_product = float(input())

    if number_of_product % 3 == 0:
        price_of_product /= 2

    total_price += price_of_product

    if budget < total_price:
        not_enough_money = True
        break

    product = input()
    number_of_product += 1

if not_enough_money:
    money_needed = total_price - budget

    print("You don't have enough money!")
    print(f"You need {money_needed:.2f} leva!")
else:
    print(f"You bought {number_of_product - 1} products for {total_price:.2f} leva.")
