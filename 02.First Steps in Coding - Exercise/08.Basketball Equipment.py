pricePerYear = int(input())

basketballShoes = pricePerYear * (1 - 0.4)
basketballJersey = basketballShoes * (1 - 0.2)
basketballBall = basketballJersey / 4
basketballAccessories = basketballBall / 5

print(pricePerYear + basketballShoes + basketballJersey + basketballBall + basketballAccessories)
