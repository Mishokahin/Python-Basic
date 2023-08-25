prices = {"one": {"Small": [9.98, 5.50], "Middle": [18.99, 4.35], "Large": [25.98, 4.35], "ExtraLarge": [35.99, 3.85]},
          "two": {"Small": [8.58, 5.50], "Middle": [17.09, 4.35], "Large": [23.59, 4.35], "ExtraLarge": [31.79, 3.85]}
          }

plan_duration = input()
plan_type = input()
data_addon = input()
months_count = int(input())
total = 0

if plan_duration in prices:
    if plan_type in prices[plan_duration]:
        if data_addon == "yes":
            total = months_count * (prices[plan_duration][plan_type][0] + prices[plan_duration][plan_type][1])
        else:
            total = months_count * prices[plan_duration][plan_type][0]

if plan_duration == "two":
    total *= (1 - (3.75/100))

print(f"{total:.2f} lv.")