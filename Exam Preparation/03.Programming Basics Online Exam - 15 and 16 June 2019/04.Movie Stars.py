budget = float(input())
name = input()

while name != "ACTION":
    if len(name) > 15:
        budget *= (1 - 0.2)
    else:
        salary = float(input())
        budget -= salary

    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        exit()

    name = input()

print(f"We are left with {budget:.2f} leva.")