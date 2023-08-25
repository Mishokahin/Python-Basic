seats = int(input())
command = input()
total = 0

while command != "Movie time!":
    seats -= int(command)
    if seats < 0:
        print(f"The cinema is full.", f"\nCinema income - {total} lv.")
        exit()

    if int(command) % 3 == 0:
        total += (int(command)*5) - 5
    else:
        total += (int(command) * 5)

    command = input()

print(f"There are {seats} seats left in the cinema.", f"\nCinema income - {total} lv.")
