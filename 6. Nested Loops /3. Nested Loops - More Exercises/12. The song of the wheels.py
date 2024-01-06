import sys

control_number = int(input())
magic_number = 0
counter = 0
password_first_number = 0
password_second_number = 0
password_third_number = 0
password_fourth_number = 0

flag = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                magic_number = a * b + c * d

                if b > a and c > d and magic_number == control_number:
                    counter += 1

                    print(f"{a}{b}{c}{d}", end=" ")

                    if counter == 4:
                        password_first_number = a
                        password_second_number = b
                        password_third_number = c
                        password_fourth_number = d

                        flag = True
                    elif counter == 0:
                        print("No!")
                        sys.exit()

if counter < 4:
    print()
    print("No!")
    sys.exit()
if flag:
    print()
    print(f"Password: {password_first_number}{password_second_number}{password_third_number}{password_fourth_number}")

