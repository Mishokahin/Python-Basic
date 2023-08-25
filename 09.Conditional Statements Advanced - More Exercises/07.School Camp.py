import sys
discounts = {range(10, 20): 0.05,
             range(20, 50): 0.15,
             range(50, sys.maxsize): 0.5}

prices_and_sport = {"girls": {"Winter": [9.6, "Gymnastics"],
                              "Spring": [7.20, "Athletics"],
                              "Summer": [15, "Volleyball"]},
                    "boys": {"Winter": [9.6, "Judo"],
                             "Spring": [7.20, "Tennis"],
                             "Summer": [15, "Football"]},
                    "mixed": {"Winter": [10, "Ski"],
                              "Spring": [9.50, "Cycling"],
                              "Summer": [20, "Swimming"]}
                    }

season = input()
group_type = input()
number_of_students = int(input())
nights = int(input())
discount = 0
sub_total = 0
sport = 0

for key in discounts:
    if number_of_students in key:
        discount = discounts[key]

if group_type in prices_and_sport:
    if season in prices_and_sport[group_type]:
        sub_total = number_of_students * prices_and_sport[group_type][season][0] * nights
        sport = prices_and_sport[group_type][season][1]

total = sub_total * (1 - discount)

print(f"{sport} {total:.2f} lv.")