import sys
import math
prices = {range(-sys.maxsize, 5001): {"Spring": 0.75, "Summer": 0.90, "Autumn": 0.75, "Winter": 1.05},
          range(5001, 10001): {"Spring": 0.95, "Summer": 1.10, "Autumn": 0.95, "Winter": 1.25},
          range(10001, sys.maxsize): {"Spring": 1.45, "Summer": 1.45, "Autumn": 1.45, "Winter": 1.45}
          }

season = input()
distance = float(input())
distance_as_key = int(math.ceil(distance))
sub_total = 0

for key in prices:
    if distance_as_key in key:
        if season in prices[key]:
            sub_total = (distance * prices[key][season]) * 4

salary = sub_total * (1 - 0.1)

print(f"{salary:.2f}")