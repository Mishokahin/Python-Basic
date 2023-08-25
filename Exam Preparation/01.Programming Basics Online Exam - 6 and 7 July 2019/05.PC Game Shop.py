games = {"Hearthstone": 0, "Fornite": 0, "Overwatch": 0, "Others": 0}
sales = int(input())

for sale in range(sales):
    game = input()
    if game in games:
        games[game] += 1
    else:
        games["Others"] += 1

hearthstone = (games["Hearthstone"]/sales) * 100
fornite = (games["Fornite"]/sales) * 100
overwatch = (games["Overwatch"]/sales) * 100
others = (games["Others"]/sales) * 100

print(f"Hearthstone - {hearthstone:.2f}%")
print(f"Fornite - {fornite:.2f}%")
print(f"Overwatch - {overwatch:.2f}%")
print(f"Others - {others:.2f}%")