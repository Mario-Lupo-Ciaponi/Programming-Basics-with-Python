count_of_numbers = int(input())

p1_count = 0
p2_count = 0
p3_count = 0

for i in range(count_of_numbers):
    number = int(input())

    if number % 2 == 0:
        p1_count += 1
    if number % 3 == 0:
        p2_count += 1
    if number % 4 == 0:
        p3_count += 1

p1_percentage = p1_count / count_of_numbers * 100
p2_percentage = p2_count / count_of_numbers * 100
p3_percentage = p3_count / count_of_numbers * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
