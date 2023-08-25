flowerPrices = {"Roses": 5, "Dahlias": 3.8, "Tulips": 2.8, "Narcissus": 3, "Gladiolus": 2.5}
flower = input()
quantity = int(input())
budget = int(input())
price = quantity * flowerPrices[flower]

if flower == "Roses":
    if quantity > 80:
        price -= price * 0.1

elif flower == "Dahlias":
    if quantity > 90:
        price -= price * 0.15

elif flower == "Tulips":
    if quantity > 80:
        price -= price * 0.15

elif flower == "Narcissus":
    if quantity < 120:
        price += price * 0.15

elif flower == "Gladiolus":
    if quantity < 80:
        price += price * 0.2

moneyLeft = budget - price
moneyNeeded = price - budget

if price <= budget:
    print(f"Hey, you have a great garden with {quantity} {flower} and {moneyLeft:.2f} leva left.")

else:
    print(f"Not enough money, you need {moneyNeeded:.2f} leva more.")