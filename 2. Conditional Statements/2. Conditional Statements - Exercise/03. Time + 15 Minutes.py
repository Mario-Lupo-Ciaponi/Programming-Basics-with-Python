minutes = int(input())
seconds = int(input()) + 15

if seconds >= 60:
    minutes += 1
    seconds %= 60

if minutes == 24:
    minutes = 0

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
