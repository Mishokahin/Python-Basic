budget = float(input())
season = input()

destination = 0
typeOfHousing = 0
moneySpent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        typeOfHousing = "Camp"
        moneySpent = budget * 0.3
    else:
        typeOfHousing = "Hotel"
        moneySpent = budget * 0.7

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        typeOfHousing = "Camp"
        moneySpent = budget * 0.4
    else:
        typeOfHousing = "Hotel"
        moneySpent = budget * 0.8

elif budget > 1000:
    destination = "Europe"
    typeOfHousing = "Hotel"
    moneySpent = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{typeOfHousing} - {moneySpent:.2f}")