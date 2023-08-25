target = int(input())
pole_height = target - 30
count = 0
unsuccessful_jumps = 0

while pole_height <= target:
    count += 1
    jump = int(input())
    if jump > pole_height:
        pole_height += 5
        unsuccessful_jumps = 0

    else:
        unsuccessful_jumps += 1

    if unsuccessful_jumps == 3:
        print(f"Tihomir failed at {pole_height}cm after {count} jumps.")
        exit()

print(f"Tihomir succeeded, he jumped over {target}cm after {count} jumps.")