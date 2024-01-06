number_of_judges = int(input())
average_grade = 0

command = input()
number_of_students = 0

while command != 'Finish':
    name_of_presentation = command
    current_average_grade = 0

    for i in range(number_of_judges):
        grade = float(input())

        current_average_grade += grade
        average_grade += grade

    current_average_grade = current_average_grade / number_of_judges
    number_of_students += 1

    print(f'{name_of_presentation} - {current_average_grade:.2f}.')

    command = input()

print(f'Student\'s final assessment is {(average_grade / (number_of_judges * number_of_students)):.2f}.')
