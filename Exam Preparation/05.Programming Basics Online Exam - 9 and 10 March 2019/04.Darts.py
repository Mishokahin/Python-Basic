multiplier = {"Single": 1, "Double": 2, "Triple": 3}
starting_points = 301
successful_shots = 0
unsuccessful_shots = 0
name = input()
field = input()

while field != "Retire":
    points = int(input())
    if field in multiplier:
        points *= (1 * multiplier[field])

    if points <= starting_points:
        starting_points -= points
        successful_shots += 1
    else:
        starting_points -= 0
        unsuccessful_shots += 1

    if starting_points == 0:
        print(f"{name} won the leg with {successful_shots} shots.")
        exit()

    field = input()

print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")