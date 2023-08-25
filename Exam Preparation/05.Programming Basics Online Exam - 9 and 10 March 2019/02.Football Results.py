results = [input().split(":"), input().split(":"), input().split(":")]

wins = [x for x in range(len(results)) if results[x][0] > results[x][1]]
loses = [x for x in range(len(results)) if results[x][0] < results[x][1]]
draws = [x for x in range(len(results)) if results[x][0] == results[x][1]]

print(f"Team won {len(wins)} games.")
print(f"Team lost {len(loses)} games.")
print(f"Drawn games: {len(draws)}")