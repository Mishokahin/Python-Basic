import sys
prices = {"90X130": 110, "100X150": 140, "130X180": 190, "200X300": 250}
discounts = {"90X130": {range(11, 31): 1.0, range(31, 61): 0.95, range(61, sys.maxsize): 0.92},
             "100X150": {range(11, 41): 1.0, range(41, 81): 0.94, range(81, sys.maxsize): 0.90},
             "130X180": {range(11, 21): 1.0, range(21, 51): 0.93, range(51, sys.maxsize): 0.88},
             "200X300": {range(11, 26): 1.0,range(26, 51): 0.91, range(51, sys.maxsize): 0.86}}

order = int(input())
size = input()
transportation = input()

if order <= 10:
    print("Invalid order")
else:
    price = 0
    for key in discounts[size]:
        if order in key:
            price = ((order * prices[size]) * discounts[size][key])
    if transportation == "With delivery":
        price += 60
    if order > 99:
        price *= 0.96

    print(f"{price:.2f} BGN")