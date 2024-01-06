desired_height_in_cm = int(input())

the_bar = desired_height_in_cm - 30
succeed_height = 0

failed = False
tries = 1

while succeed_height < desired_height_in_cm:
    jump = int(input())

    current_tries = 0

    while jump <= the_bar:
        current_tries += 1

        if current_tries == 3:
            failed = True
            break

        tries += 1
        jump = int(input())

    if failed:
        break

    succeed_height = jump
    the_bar += 5

    tries += 1

if failed:
    print(f'Tihomir failed at {the_bar}cm after {tries} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {desired_height_in_cm}cm after {tries - 1} jumps.')
