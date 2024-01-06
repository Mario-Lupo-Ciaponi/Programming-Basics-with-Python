number_of_clients = int(input())

average_bill_per_client = 0

for i in range(number_of_clients):
    products_purchased = 0
    bill_of_client = 0
    products_bought = 0

    decoration = input()
    while decoration != "Finish":
        if decoration == "basket":
            bill_of_client += 1.5
        elif decoration == "wreath":
            bill_of_client += 3.8
        else:
            bill_of_client += 7

        products_bought += 1

        decoration = input()

    if products_bought % 2 == 0:
        bill_of_client -= bill_of_client * 0.2

    average_bill_per_client += bill_of_client

    print(f"You purchased {products_bought} items for {bill_of_client:.2f} leva.")

print(f"Average bill per client is: {(average_bill_per_client / number_of_clients):.2f} leva.")
