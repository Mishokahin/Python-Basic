import math
points = {"W": 2000, "F": 1200, "SF": 720}
tournaments_count = int(input())
starting_points = int(input())
results = [input() for x in range(tournaments_count)]
game_points = [points[x] for x in results]
wins = [x for x in results if x == "W"]

print(f"Final points: {starting_points + sum(game_points)}")
print(f"Average points: {math.floor(sum(game_points)/tournaments_count)}")
print(f"{(len(wins)/tournaments_count)*100:.2f}%")