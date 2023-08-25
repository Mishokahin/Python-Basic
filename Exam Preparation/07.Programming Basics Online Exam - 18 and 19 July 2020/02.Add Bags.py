import sys
import math
prices = {range(-sys.maxsize, 10): 0.2, range(10, 21): 0.5, range(21, sys.maxsize): 1}
penalties = {range(-sys.maxsize, 7): 0.4, range(7, 31): 0.15, range(31, sys.maxsize): 0.1}
price_luggage_over_30 = float(input())
luggage_weight = float(input())
days_before = int(input())
luggage_count = int(input())
price = 0
for i in prices:
    if math.ceil(luggage_weight) in i:
        price = price_luggage_over_30 * prices[i]

penalty = 0
for i in penalties:
    if days_before in i:
        penalty = price * penalties[i]

total = (price + penalty) * luggage_count

print(f"The total price of bags is: {total:.2f} lv.")