number_of_tournaments = int(input())

days_won = 0
days_lost = 0

money_won = 0

for i in range(number_of_tournaments):
    sport = input()

    current_money_won = 0

    games_won = 0
    games_lost = 0

    while sport != "Finish":
        result = input()

        if result == "win":
            current_money_won += 20
            games_won += 1
        else:
            games_lost += 1

        sport = input()

    if games_won > games_lost:
        current_money_won += current_money_won * 0.1
        days_won += 1
    else:
        days_lost += 1

    money_won += current_money_won

if days_won > days_lost:
    money_won += money_won * 0.2
    print(f"You won the tournament! Total raised money: {money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_won:.2f}")
