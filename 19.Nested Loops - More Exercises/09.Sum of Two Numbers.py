loop_start = int(input())
loop_end = int(input())
magic_number = int(input())
count = 0

for x1 in range(loop_start, loop_end + 1):
    for x2 in range(loop_start, loop_end + 1):
        count += 1
        if x1 + x2 == magic_number:
            print(f"Combination N:{count} ({x1} + {x2} = {magic_number})")
            exit()

print(f"{count} combinations - neither equals {magic_number}")