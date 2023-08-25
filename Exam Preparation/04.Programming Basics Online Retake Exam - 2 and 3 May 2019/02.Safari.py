budget = float(input())
gas = float(input()) * 2.1
day = input()
total = gas + 100

if day == "Sunday":
    total *= (1 - 0.2)
else:
    total *= (1 - 0.1)

money = abs(budget - total)

print(f"Safari time! Money left: {money:.2f} lv." if total <= budget
      else f"Not enough money! Money needed: {money:.2f} lv.")