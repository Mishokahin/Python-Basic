juniors_prices = {"trail": 5.50, "cross-country": 8, "downhill": 12.25, "road": 20}
seniors_prices = {"trail": 7, "cross-country": 9.5, "downhill": 13.75, "road": 21.5}

junior_bikers = int(input())
senior_bikers = int(input())
race_type = input()

total_bikers = junior_bikers + senior_bikers

if race_type in juniors_prices:
    if race_type == "cross-country" and total_bikers >= 50:
        junior_bikers_total = junior_bikers * (juniors_prices[race_type] * (1 - 0.25))
    else:
        junior_bikers_total = junior_bikers * juniors_prices[race_type]

if race_type in seniors_prices:
    if race_type == "cross-country" and total_bikers >= 50:
        senior_bikers_total = senior_bikers * (seniors_prices[race_type] * (1 - 0.25))
    else:
        senior_bikers_total = senior_bikers * seniors_prices[race_type]

sub_total = junior_bikers_total + senior_bikers_total
expenses = sub_total * 0.05
total = sub_total - expenses

print(f"{total:.2f}")

