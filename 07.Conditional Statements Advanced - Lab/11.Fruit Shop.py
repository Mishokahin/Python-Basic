weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekdayPrices = {"banana": 2.5, "apple": 1.2, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.70, "pineapple": 5.50, "grapes": 3.85}
weekend = ["saturday", "sunday"]
weekendPrices = {"banana": 2.7, "apple": 1.25, "orange": 0.9, "grapefruit": 1.60, "kiwi": 3.00, "pineapple": 5.60, "grapes": 4.20}

fruit = input().lower()
day = input().lower()
quantity = float(input())
price = 0

if day in weekdays:
    if fruit in weekdayPrices:
        price = weekdayPrices[fruit] * quantity
        print(f"{price:.2f}")
    else:
        print("error")
elif day in weekend:
    if fruit in weekendPrices:
        price = weekendPrices[fruit] * quantity
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")