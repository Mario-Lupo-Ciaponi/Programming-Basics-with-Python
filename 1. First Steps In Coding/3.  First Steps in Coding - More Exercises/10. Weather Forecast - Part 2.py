degrees = float(input())
weather = ''

if degrees >= 5 and degrees <= 11.9:
    weather = 'Cold'
elif degrees >= 12 and degrees <= 14.9:
    weather = 'Cool'
elif degrees >= 15 and degrees <= 20:
    weather = 'Mild'
elif degrees >= 20.1 and degrees <= 25.9:
    weather = 'Warm'
elif degrees >= 26 and degrees <= 35:
    weather = 'Hot'
else:
    weather = 'unknown'

print(weather)
