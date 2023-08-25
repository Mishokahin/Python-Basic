prices = {"Dubai": {"Summer": 40000, "Winter": 45000},
          "Sofia": {"Summer": 12500, "Winter": 17000},
          "London": {"Summer": 20250, "Winter": 24000}
          }

budget = float(input())
destination = input()
season = input()
days_count = int(input())
total = 0

if destination in prices:
    if season in prices[destination]:
        if destination == "Dubai":
            total = (days_count * prices[destination][season]) * (1 - 0.3)
        elif destination == "Sofia":
            total = (days_count * prices[destination][season]) * (1 + 0.25)
        else:
            total = days_count * prices[destination][season]

money_left = abs(budget - total)

print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!" if total <= budget
      else f"The director needs {money_left:.2f} leva more!")