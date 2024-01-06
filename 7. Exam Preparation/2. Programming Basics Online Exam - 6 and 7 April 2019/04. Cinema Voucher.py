value_of_voucher = int(input())

item = input()
price = 0

count_of_tickets = 0
count_of_other_items = 0

while item != "End":
    is_ticket = False
    is_other_item = False

    if len(item) > 8:
        price += ord(item[0]) + ord(item[1])
        is_ticket = True
    else:
        price += ord(item[0])
        is_other_item = True

    if price > value_of_voucher:
        break

    if is_ticket:
        count_of_tickets += 1
    if is_other_item:
        count_of_other_items += 1

    item = input()

print(count_of_tickets)
print(count_of_other_items)
