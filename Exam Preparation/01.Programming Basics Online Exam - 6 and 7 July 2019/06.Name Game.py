name = input()
points = 0
winner_name = ""

while name != "Stop":
    current_name = name
    current_points = 0
    for char in name:
        number = int(input())
        if number == ord(char):
            current_points += 10
        else:
            current_points += 2

    if current_points >= points:
        points = current_points
        winner_name = current_name

    name = input()

print(f"The winner is {winner_name} with {points} points!")