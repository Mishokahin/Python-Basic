chef_count = int(input())
top_chef = ""
top_score = 0

for i in range(chef_count):
    name = input()
    current_points = 0
    points = input()
    while points != "Stop":
        current_points += int(points)
        points = input()

    print(f"{name} has {current_points} points.")

    if current_points > top_score:
        top_score = current_points
        top_chef = name
        print(f"{name} is the new number 1!")

print(f"{top_chef} won competition with {top_score} points!")