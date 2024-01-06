import math

record_in_seconds = float(input())
distance_in_meters = float(input())
meters_per_second = float(input())

time_without_water_resistance= distance_in_meters * meters_per_second
resistance_of_water = math.floor(distance_in_meters / 15)
total_resistance_of_water = resistance_of_water * 12.5

time_of_ivan = time_without_water_resistance + total_resistance_of_water

if time_of_ivan < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {time_of_ivan:.2f} seconds.')
else:
    seconds_needed = time_of_ivan - record_in_seconds
    print(f'No, he failed! He was {seconds_needed:.2f} seconds slower.')
