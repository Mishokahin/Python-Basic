capacity = float(input())
count = 0
statistic = 0
load = input()
while load != "End":
    count += 1
    if count % 3 == 0:
        capacity -= float(load) * 1.1
    else:
        capacity -= float(load)

    if capacity < 0:
        print("No more space!")
        print(f"Statistic: {statistic} suitcases loaded.")
        exit()

    statistic += 1

    load = input()

print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {statistic} suitcases loaded.")