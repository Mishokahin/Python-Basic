width = int(input())
length = int(input())


cake_left = width * length

while cake_left > 0:
    command = input()
    if command == "STOP":
        break
    cake_left -= int(command)

if cake_left < 0:
    print(f"No more cake left! You need {abs(cake_left)} pieces more.")
else:
    print(f"{cake_left} pieces are left.")