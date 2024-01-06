count_of_packets_of_pens = int(input())
count_of_packets_of_markers = int(input())
liters_of_chalkboard_cleaner = int(input())
discount = int(input())

price_of_pens = count_of_packets_of_pens * 5.8
price_of_markers = count_of_packets_of_markers * 7.2
price_of_chalkboard_cleaner = liters_of_chalkboard_cleaner * 1.2

price_without_discount = price_of_pens + price_of_markers + price_of_chalkboard_cleaner
price_with_discount = price_without_discount - price_without_discount * (discount / 100)

print(price_with_discount)
