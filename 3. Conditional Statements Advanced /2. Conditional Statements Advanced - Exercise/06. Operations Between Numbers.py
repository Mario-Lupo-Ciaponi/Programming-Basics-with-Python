first_number = int(input())
second_number = int(input())
operation = input()

even_or_odd = ''
invalid_operation = False
result = 0

if operation == '+':
    result = first_number + second_number

    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
elif operation == '-':
    result = first_number - second_number
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
elif operation == '*':
    result = first_number * second_number

    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
elif operation == '/':
    if first_number == 0 or second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f'{first_number} / {second_number} = {result:.2f}')
else:
    if first_number == 0 or second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f'{first_number} % {second_number} = {result}')
