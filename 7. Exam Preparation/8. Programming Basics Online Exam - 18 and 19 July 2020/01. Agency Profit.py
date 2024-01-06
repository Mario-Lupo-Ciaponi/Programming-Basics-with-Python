airline_name = input()
count_of_adult_tickets = int(input())
count_of_kid_tickets = int(input())
net_price_for_adult_tickets = float(input())
servie_fee = float(input())

net_price_for_kid_ticket = net_price_for_adult_tickets - net_price_for_adult_tickets * 0.7

total_price_for_adult_ticket = count_of_adult_tickets * (net_price_for_adult_tickets + servie_fee)
total_price_for_kid_ticket = count_of_kid_tickets * (net_price_for_kid_ticket + servie_fee)

total_price = total_price_for_adult_ticket + total_price_for_kid_ticket

print(f"The profit of your agency from {airline_name} tickets is {(total_price * 0.2):.2f} lv.")
