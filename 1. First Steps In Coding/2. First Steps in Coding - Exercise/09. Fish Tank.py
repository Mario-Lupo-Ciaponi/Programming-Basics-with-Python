length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent = int(input())

volume_of_aquaruim = length_in_cm * width_in_cm * height_in_cm
volume_of_aquaruim_in_liters = volume_of_aquaruim / 1000

true_percent = percent / 100

total_volume = volume_of_aquaruim_in_liters * (1 - true_percent)

print(total_volume)
