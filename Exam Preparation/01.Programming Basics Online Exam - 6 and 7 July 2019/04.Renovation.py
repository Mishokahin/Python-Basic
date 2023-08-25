import math
wall_height = int(input())
wall_width = int(input())
percent_to_skip = int(input())

wall_sqm = wall_width * wall_height * 4
sqm_to_paint = math.ceil(wall_sqm * (1 - (percent_to_skip/100)))

command = input()

while command != "Tired!":
    sqm_to_paint -= int(command)
    if sqm_to_paint <= 0:
        break
    command = input()

if sqm_to_paint == 0:
    print("All walls are painted! Great job, Pesho!")
elif sqm_to_paint < 0:
    print(f"All walls are painted and you have {abs(math.ceil(sqm_to_paint))} l paint left!" )
else:
    print(f"{math.ceil(sqm_to_paint)} quadratic m left." )