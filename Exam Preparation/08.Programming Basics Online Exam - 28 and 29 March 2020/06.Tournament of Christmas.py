tournaments_count = int(input())
days_won, days_lost, total_money = 0, 0, 0

for i in range(tournaments_count):
    current_money, current_wins, current_loses = 0, 0, 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            current_money += 20
            current_wins += 1
        else:
            current_loses += 1

        sport = input()
    if current_wins > current_loses:
        current_money *= 1.1
        days_won += 1
    else:
        days_lost += 1

    total_money += current_money

if days_won > days_lost:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")

else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")