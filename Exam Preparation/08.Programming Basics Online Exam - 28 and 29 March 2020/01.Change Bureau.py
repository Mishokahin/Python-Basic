prices = {"bitcoin": 1168, "yuan": 0.15, "dollar": 1.76, "euro": 1.95}
bitcoin_count = int(input())
yuan_count = float(input())
commission = float(input())

sub_total = [bitcoin_count * prices["bitcoin"], (yuan_count * prices["yuan"]) * prices["dollar"]]

print(f"{sum(sub_total)/prices['euro']*(1-commission/100):.2f}")
