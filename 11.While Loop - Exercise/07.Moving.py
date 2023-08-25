width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

while total_space > 0:
    command = input()
    if command == "Done":
        break
    total_space -= int(command)

if total_space < 0:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
else:
    print(f"{total_space} Cubic meters left.")