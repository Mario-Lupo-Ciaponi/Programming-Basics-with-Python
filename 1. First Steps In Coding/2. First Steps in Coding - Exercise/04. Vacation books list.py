import math

number_of_pages = int(input())
pages_read_per_hour = int(input())
days_remaining = int(input())

hours_needed_for_reading = number_of_pages / pages_read_per_hour
hours_per_day = hours_needed_for_reading / days_remaining

print(math.floor(hours_per_day))