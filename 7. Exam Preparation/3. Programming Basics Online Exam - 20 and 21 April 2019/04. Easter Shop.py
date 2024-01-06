quantity_of_eggs = int(input())

not_enough_eggs = False
eggs_sold = 0

command = input()
while command != "Close":
    eggs_for_command = int(input())

    if command == "Buy":
        if eggs_for_command > quantity_of_eggs:
            not_enough_eggs = True
            break
        else:
            quantity_of_eggs -= eggs_for_command
            eggs_sold += eggs_for_command
    else:
        quantity_of_eggs += eggs_for_command

    command = input()

if not_enough_eggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {quantity_of_eggs}.")
else:
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")
