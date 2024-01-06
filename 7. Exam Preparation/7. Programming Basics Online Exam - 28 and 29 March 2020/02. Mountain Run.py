import math

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

distance_without_slope = distance_in_meters * seconds_per_meter
slope = math.floor(distance_in_meters / 50)
total_slope = slope * 30

total_distance = distance_without_slope + total_slope

if total_distance < record_in_seconds:
    print(f"Yes! The new record is {total_distance:.2f} seconds.")
else:
    seconds_slower = total_distance - record_in_seconds
    print(f"No! He was {seconds_slower:.2f} seconds slower.")
