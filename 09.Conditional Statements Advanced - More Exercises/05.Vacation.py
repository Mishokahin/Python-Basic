import sys
import math
accommodation = {range(-sys.maxsize, 1001): "Camp",
                 range(1001, 3001): "Hut",
                 range(3001, sys.maxsize): "Hotel"
                 }
prices = {"Camp": {"Summer": ["Alaska", 0.65], "Winter": ["Morocco", 0.45]},
          "Hut": {"Summer": ["Alaska", 0.80], "Winter": ["Morocco", 0.60]},
          "Hotel": {"Summer": ["Alaska", 0.90], "Winter": ["Morocco", 0.90]}
          }

budget = float(input())
budget_as_key = int(math.ceil(budget))
season = input()
accommodation_type = 0
destination = 0
price = 0

for key in accommodation:
    if budget_as_key in key:
        accommodation_type = accommodation[key]
        break

if accommodation_type in prices:
    if season in prices[accommodation_type]:
        destination = prices[accommodation_type][season][0]
        price = budget * prices[accommodation_type][season][1]

print(f"{destination} - {accommodation_type} - {price:.2f}")