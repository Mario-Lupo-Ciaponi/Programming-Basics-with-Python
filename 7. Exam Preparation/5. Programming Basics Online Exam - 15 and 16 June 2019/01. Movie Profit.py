movie_name = input()
count_of_days = int(input())
count_of_tickets = int(input())
price_of_ticket = float(input())
percent_of_cinema = int(input())

price_for_a_day = count_of_tickets * price_of_ticket

total_price = count_of_days * price_for_a_day
total_percent = total_price * (percent_of_cinema / 100)

print(f"The profit from the movie {movie_name} is {(total_price - total_percent):.2f} lv.")
