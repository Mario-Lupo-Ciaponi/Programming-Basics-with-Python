last_sector = ord(input())
number_of_rows_in_first_sector = int(input())
places_in_odd_rows = int(input())
places_in_even_rows = places_in_odd_rows + 2

number_of_rows_in_sector = number_of_rows_in_first_sector
row = 1
counter = 0

for sector in range(ord('A'), last_sector + 1):
    for row in range(1, number_of_rows_in_sector + 1):
        if row % 2 != 0:
            for i in range(ord('a'), (ord('a') + places_in_odd_rows)):
                print(f'{chr(sector)}{row}{chr(i)}')
                counter += 1
        elif row % 2 == 0:
            for i in range(ord('a'), (ord('a') + places_in_even_rows)):
                print(f'{chr(sector)}{row}{chr(i)}')
                counter += 1

    number_of_rows_in_sector += 1

print(counter)
