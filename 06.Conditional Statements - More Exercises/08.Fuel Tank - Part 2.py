fuel_prices = {"Diesel": 2.33, "Gasoline": 2.22, "Gas": 0.93}
card_discounts = {"Diesel": 0.12, "Gasoline": 0.18, "Gas": 0.08}

fuel = input()
fuel_quantity = float(input())
card = input()

if fuel_quantity > 25:
    discount = 0.1

elif 20 <= fuel_quantity <= 25:
    discount = 0.08

else:
    discount = 0

if fuel in fuel_prices:
    if card == "No":
        fuel_price = fuel_prices[fuel]
    else:
        fuel_price = fuel_prices[fuel] - card_discounts[fuel]

sub_total = fuel_quantity * fuel_price
total = sub_total - (sub_total * discount)

print(f"{total:.2f} lv.")