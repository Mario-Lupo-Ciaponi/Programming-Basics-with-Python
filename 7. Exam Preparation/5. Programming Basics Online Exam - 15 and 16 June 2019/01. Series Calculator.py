import math

series_name = input()

number_of_seasons = int(input())
count_of_episodes = int(input())
normal_episode_duration = float(input())

ads_duration = normal_episode_duration * 0.2
total_episode_duration = normal_episode_duration + ads_duration

special_episode_duration = number_of_seasons * 10

total_duration = total_episode_duration * count_of_episodes * number_of_seasons + special_episode_duration

print(f"Total time needed to watch the {series_name} series is {math.floor(total_duration)} minutes.")
