drink_prices = {"Espresso": {"Without": 0.9, "Normal": 1, "Extra": 1.2},
                "Cappuccino": {"Without": 1, "Normal": 1.2, "Extra": 1.6},
                "Tea": {"Without": 0.5, "Normal": 0.6, "Extra": 0.7}
                }
drink = input()
option = input()
drink_count = int(input())
total = 0

if drink in drink_prices:
    if option in drink_prices[drink]:
        total = drink_prices[drink][option] * drink_count

if option == "Without":
    total *= (1 - 0.35)

if drink == "Espresso" and drink_count > 5:
    total *= (1 - 0.25)

if total > 15:
    total *= (1 - 0.2)

print(f"You bought {drink_count} cups of {drink} for {total:.2f} lv.")