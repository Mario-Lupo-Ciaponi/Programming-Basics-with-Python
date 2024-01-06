number_of_students = int(input())

excellent_count = 0
good_count = 0
mid_count = 0
failed_count = 0

total_grades = 0

for i in range(number_of_students):
    grade = float(input())

    if 2 <= grade <= 2.99:
        failed_count += 1
    elif 3 <= grade <= 3.99:
        mid_count += 1
    elif  4 <= grade <= 4.99:
        good_count += 1
    else:
        excellent_count += 1

    total_grades += grade

average_grade = total_grades / number_of_students

excellent_percent = excellent_count / number_of_students * 100
good_percent = good_count / number_of_students * 100
mid_percent = mid_count / number_of_students * 100
failed_percent = failed_count / number_of_students * 100

print(f'Top students: {excellent_percent:.2f}%')
print(f'Between 4.00 and 4.99: {good_percent:.2f}%')
print(f'Between 3.00 and 3.99: {mid_percent:.2f}%')
print(f'Fail: {failed_percent:.2f}%')
print(f'Average: {average_grade:.2f}')
