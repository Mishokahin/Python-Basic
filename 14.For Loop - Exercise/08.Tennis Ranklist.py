import math
point_map = {"W": 2000, "F": 1200, "SF": 720}
number_of_tournaments = int(input())
starting_points = int(input())

points_won = 0
wins = 0

for n in range(number_of_tournaments):
    outcome = input()
    if outcome in point_map:
        points_won += point_map[outcome]
    if outcome == "W":
        wins += 1

average_point = math.floor(points_won/number_of_tournaments)
winning_percentage = (wins/number_of_tournaments) * 100

print(f"Final points: {points_won + starting_points}")
print(f"Average points: {average_point}")
print(f"{winning_percentage:.2f}%")