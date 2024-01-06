minutes_of_walking_per_stroll = int(input())
number_of_strolls_per_day = int(input())
calories_taken = int(input())

total_minutes_of_walking = minutes_of_walking_per_stroll * number_of_strolls_per_day
total_calories_burnt = total_minutes_of_walking * 5

if total_calories_burnt >= calories_taken / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burnt}.")
