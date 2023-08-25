budget = int(input())
season = input()
fishermen = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
else:
    price = 2600

if fishermen <= 6:
    price *= 0.9

elif 7 <= fishermen <= 11:
    price *= 0.85

elif fishermen > 12:
    price *= 0.75

if fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95

moneyLeft = budget - price
moneyNeeded = price - budget

if price <= budget:
    print(f"Yes! You have {moneyLeft:.2f} leva left.")

else:
    print(f"Not enough money! You need {moneyNeeded:.2f} leva.")