prices = {range(0, 6): {"spring": 50.00, "summer": 48.50, "autumn": 60.00, "winter": 86.00},
          range(6, 21): {"spring": 48.00, "summer": 45.00, "autumn": 49.50, "winter": 85.00}}

guest_count = int(input())
season = input()
total = 0
for key in prices:
    if guest_count in key:
        total = guest_count * prices[key][season]

if season == "summer":
    total *= 0.85

if season == "winter":
    total *= 1.08

print(f"{total:.2f} leva.")