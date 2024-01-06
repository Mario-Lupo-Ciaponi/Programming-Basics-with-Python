minutes_of_control = int(input())
seconds_of_control = int(input())
length_of_the_chute_in_meters = float(input())
seconds_of_100_meters = int(input())

total_control_in_seconds = minutes_of_control * 60 + seconds_of_control

decreasing_time = length_of_the_chute_in_meters / 120
total_decreasing_time = decreasing_time * 2.5

marin_time = (length_of_the_chute_in_meters / 100) * seconds_of_100_meters - total_decreasing_time

if marin_time < total_control_in_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    seconds_slower = marin_time - total_control_in_seconds
    print(f'No, Marin failed! He was {seconds_slower:.3f} second slower.')
