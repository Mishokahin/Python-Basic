n = int(input())
total_points = 0
others = 0
points = {"red": 5, "orange": 10, "yellow": 15, "white": 20}
colors = {"red": 0, "orange": 0, "yellow": 0, "white": 0, "black": 0, "other": 0}

for i in range(n):
    color = input()
    if color in points:
        total_points += points[color]
        colors[color] += 1
    elif color == "black":
        total_points /= 2
        colors[color] += 1
    else:
        colors["other"] += 1

print(f"Total points: {int(total_points)}")
print(f"Red balls: {colors['red']}")
print(f"Orange balls: {colors['orange']}")
print(f"Yellow balls: {colors['yellow']}")
print(f"White balls: {colors['white']}")
print(f"Other colors picked: {colors['other']}")
print(f"Divides from black balls: {colors['black']}")