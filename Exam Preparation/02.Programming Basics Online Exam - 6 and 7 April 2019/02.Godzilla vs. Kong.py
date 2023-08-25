filmBudget = float(input())
numberOfExtras = int(input())
pricePerCostume = float(input())

decorePrice = filmBudget * 0.1
costumesPrice = numberOfExtras * pricePerCostume

if numberOfExtras > 150:
    costumesPrice *= (1 - 0.1)

if decorePrice + costumesPrice <= filmBudget:
    print("Action!")
    print(f"Wingard starts filming with {abs(filmBudget - (decorePrice + costumesPrice)):.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {abs(filmBudget - (decorePrice + costumesPrice)):.2f} leva more.")