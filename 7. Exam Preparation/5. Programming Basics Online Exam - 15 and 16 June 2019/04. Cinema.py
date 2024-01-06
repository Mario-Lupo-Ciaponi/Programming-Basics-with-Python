hall_capacity = int(input())

total_income = 0
total_people = 0

command = input()

while command != "Movie time!":
    people_in_cinema = int(command)
    total_people += people_in_cinema

    if hall_capacity < total_people:
        print("The cinema is full.")
        break

    income = people_in_cinema * 5

    if people_in_cinema % 3 == 0:
        income -= 5

    total_income += income

    command = input()

if hall_capacity >= total_people:
    seats_left = hall_capacity - total_people
    print(f"There are {seats_left} seats left in the cinema.")

print(f"Cinema income - {total_income} lv.")
