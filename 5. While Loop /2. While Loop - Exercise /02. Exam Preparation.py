import sys

limit_of_unsatisfying_grades = int(input())

average_score = 0
number_of_problems = 0
last_problem = 0

count_of_unsatisfying_grades = 0

name_of_exercise = input()

while name_of_exercise != 'Enough':
    last_problem = name_of_exercise
    grade = int(input())

    if grade <= 4:
        count_of_unsatisfying_grades += 1

    if count_of_unsatisfying_grades == limit_of_unsatisfying_grades:
        print(f'You need a break, {count_of_unsatisfying_grades} poor grades.')
        sys.exit()

    average_score += grade
    number_of_problems += 1

    name_of_exercise = input()

print(f'Average score: {(average_score / number_of_problems):.2f}')
print(f'Number of problems: {number_of_problems}')
print(f'Last problem: {last_problem}')
