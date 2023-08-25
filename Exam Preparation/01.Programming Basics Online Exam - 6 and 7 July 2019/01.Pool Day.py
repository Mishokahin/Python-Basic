import math
people_count = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

entrance_total = people_count * entrance_fee
sunbed_total = math.ceil(people_count * 0.75) * sunbed_price
umbrella_total = math.ceil(people_count * 0.5) * umbrella_price
total = entrance_total + sunbed_total + umbrella_total

print(f"{total:.2f} lv.")