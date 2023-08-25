load = input()
total_detergent = int(load) * 750
command = input()
dishes = 0
pots = 0
counter = 0

while command != "End":
    counter += 1
    if counter % 3 == 0:
        pots += int(command)
        total_detergent -= int(command) * 15
    else:
        dishes += int(command)
        total_detergent -= int(command) * 5

    if total_detergent < 0:
        break

    command = input()

if total_detergent >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
