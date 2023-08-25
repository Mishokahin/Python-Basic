import string
seat_map = string.ascii_lowercase
final_sector = input()
rows = int(input())
seats = int(input())
count = 0

for sector in string.ascii_uppercase:
    if sector > final_sector:
        break
    for row in range(1, rows + 1):
        if row % 2 == 0:
            for seat in range(seats+2):
                print(f"{sector}{row}{seat_map[seat]}")
                count += 1
        else:
            for seat in range(seats):
                print(f"{sector}{row}{seat_map[seat]}")
                count += 1
    rows += 1

print(count)