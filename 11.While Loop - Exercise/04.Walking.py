goal = 10000
steps_walked = 0

while steps_walked < goal:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        steps_walked += steps
        break
    else:
        steps_walked += int(steps)

steps_difference = abs(goal - steps_walked)

if steps_walked < goal:
    print(f"{steps_difference} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{steps_difference} steps over the goal!")