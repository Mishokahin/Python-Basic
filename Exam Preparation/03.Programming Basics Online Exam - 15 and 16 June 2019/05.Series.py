discounts = {"Thrones": 0.50, "Lucifer": 0.40, "Protector": 0.30, "TotalDrama": 0.20, "Area": 0.10}
budget = float(input())
n = int(input())

for i in range(n):
    name = input()
    price = float(input())
    if name in discounts:
        price *= (1 - discounts[name])
    budget -= price

print(f"You need {abs(budget):.2f} lv. more to buy the series!" if budget < 0
      else f"You bought all the series and left with {budget:.2f} lv.")