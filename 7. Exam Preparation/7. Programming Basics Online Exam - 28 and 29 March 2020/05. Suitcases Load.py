capacity_of_trunk = float(input())
space_taken = 0
number_of_suitcases = 0

no_more_space = False

command = input()
while command != "End":
    current_space_taken = float(command)
    number_of_suitcases += 1

    if number_of_suitcases % 3 == 0:
        current_space_taken += current_space_taken * 0.1

    space_taken += current_space_taken

    if space_taken > capacity_of_trunk:
        no_more_space = True
        break

    command = input()

if no_more_space:
    print("No more space!")
    number_of_suitcases -= 1
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {number_of_suitcases} suitcases loaded.")
