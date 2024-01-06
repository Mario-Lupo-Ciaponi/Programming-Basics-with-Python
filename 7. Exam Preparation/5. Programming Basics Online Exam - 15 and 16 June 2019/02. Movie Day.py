time_for_recording = int(input())
count_of_scenes = int(input())
duration_of_a_scene = int(input())

terrain_preparation = time_for_recording * 0.15

time_for_scenes = count_of_scenes * duration_of_a_scene

time_needed = terrain_preparation + time_for_scenes

if time_for_recording >= time_needed:
    time_left = round(time_for_recording - time_needed)
    print(f"You managed to finish the movie on time! You have {time_left} minutes left!")
else:
    time_that_is_not_enough = round(time_needed - time_for_recording)
    print(f"Time is up! To complete the movie you need {time_that_is_not_enough} minutes.")
