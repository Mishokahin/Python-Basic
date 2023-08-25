nylonSqM = int(input())
paintLiters = int(input())
paintThinnerLiters = int(input())
workersHours = int(input())

materialsCost = ((nylonSqM + 2) * 1.50) + ((paintLiters + (paintLiters * 0.1)) * 14.50) + paintThinnerLiters * 5.00 + 0.4
workersWage = (materialsCost * 0.3) * workersHours

print(materialsCost + workersWage)