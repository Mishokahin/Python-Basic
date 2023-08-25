import sys
import math
classes = {range(-sys.maxsize, 101): "Economy class",
           range(101, 501): "Compact class",
           range(501, sys.maxsize): "Luxury class"
           }
prices = {"Economy class": {"Summer": ["Cabrio", 0.35], "Winter": ["Jeep", 0.65]},
          "Compact class": {"Summer": ["Cabrio", 0.45], "Winter": ["Jeep", 0.80]},
          "Luxury class": {"Summer": ["Jeep", 0.90], "Winter": ["Jeep", 0.90]}
          }

budget = float(input())
budget_as_key = int(math.ceil(budget))
season = input()
vehicle_class = 0
vehicle_type = 0
vehicle_price = 0

for key in classes:
    if budget_as_key in key:
        vehicle_class = classes[key]
        break

if vehicle_class in prices:
    if season in prices[vehicle_class]:
        vehicle_type = prices[vehicle_class][season][0]
        vehicle_price = budget * prices[vehicle_class][season][1]

print(f"{vehicle_class}")
print(f"{vehicle_type} - {vehicle_price:.2f}")