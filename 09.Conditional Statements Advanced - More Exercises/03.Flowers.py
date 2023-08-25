flower_prices = {"Spring": [2.00, 4.10, 2.50],
                 "Summer": [2.00, 4.10, 2.50],
                 "Autumn": [3.75, 4.50, 4.15],
                 "Winter": [3.75, 4.50, 4.15]
                 }

chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_holiday = input()

total_flowers = chrysanthemums + roses + tulips
flowers_cost = 0
holiday_increase = 0

if season in flower_prices:
    flowers_cost = (chrysanthemums * flower_prices[season][0]) + (roses * flower_prices[season][1]) +\
                   (tulips * flower_prices[season][2])

if is_holiday == "Y":
    holiday_increase = flowers_cost * 0.15

sub_total = flowers_cost + holiday_increase

if tulips > 7 and season == "Spring":
    sub_total *= (1 - 0.05)

if roses >= 10 and season == "Winter":
    sub_total *= (1 - 0.1)

if total_flowers > 20:
    sub_total *= (1 - 0.2)

total = sub_total + 2

print(f"{total:.2f}")