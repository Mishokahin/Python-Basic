tournament_name = input()
number_or_matches = 0
number_of_wins = 0
number_of_loses = 0

while tournament_name != "End of tournaments":
    number_of_games = int(input())
    for i in range(1, number_of_games+1):
        desi_points = int(input())
        opponent_points = int(input())
        if desi_points > opponent_points:
            print(f"Game {i} of tournament {tournament_name}: win with {desi_points - opponent_points} points.")
            number_of_wins += 1
        else:
            print(f"Game {i} of tournament {tournament_name}: lost with {opponent_points - desi_points} points.")
            number_of_loses += 1

    number_or_matches += number_of_games
    tournament_name = input()

print(f"{(number_of_wins/number_or_matches)*100:.2f}% matches win")
print(f"{(number_of_loses/number_or_matches)*100:.2f}% matches lost")