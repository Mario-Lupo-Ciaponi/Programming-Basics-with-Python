volume_of_pool = int(input())
p1_work_for_hour = int(input())
p2_work_for_hour = int(input())
hours_worker_was_away = float(input())

p1_total_work = p1_work_for_hour * hours_worker_was_away
p2_total_work = p2_work_for_hour * hours_worker_was_away

total_work = p1_total_work + p2_total_work

if total_work <= volume_of_pool:
    p1_percentage = p1_total_work / total_work * 100
    p2_percentage = p2_total_work / total_work * 100

    total_percentage = total_work / volume_of_pool * 100

    print(f'The pool is {total_percentage:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}')
else:
    overflow_litters = total_work - volume_of_pool

    print(f'For {hours_worker_was_away:.2f} hours the pool overflows with {overflow_litters:.2f} liters.')
