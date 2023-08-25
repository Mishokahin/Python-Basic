import math
magnolia_quantity = int(input())
hyacinth_quantity = int(input())
roses_quantity = int(input())
cacti_quantity = int(input())
gift_cost = float(input())

sub_total = (magnolia_quantity * 3.25) + (hyacinth_quantity * 4) + (roses_quantity * 3.50) + (cacti_quantity * 8)
profit = sub_total * (1 - 0.05)

if profit >= gift_cost:
    money_left = math.floor(profit - gift_cost)
    print(f"She is left with {money_left} leva.")

else:
    money_needed = math.ceil(gift_cost - profit)
    print(f"She will have to borrow {money_needed} leva.")