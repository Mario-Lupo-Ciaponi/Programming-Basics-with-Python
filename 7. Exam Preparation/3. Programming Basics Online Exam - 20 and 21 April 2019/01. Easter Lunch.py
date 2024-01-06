count_of_kozunaks = int(input())
count_of_crusts = int(input())
kg_of_cookies = int(input())
count_of_eggs = count_of_crusts * 12

price_of_kozunak = count_of_kozunaks * 3.2
price_of_crusts = count_of_crusts * 4.35
price_of_cookies = kg_of_cookies * 5.4
price_of_paint = count_of_eggs * 0.15

total_price = price_of_kozunak + price_of_crusts + price_of_cookies + price_of_paint

print(f"{total_price:.2f}")
