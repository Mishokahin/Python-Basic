budget = float(input())
product_name = input()
count = 0
items = 0
total = 0

while product_name != "Stop":
    count += 1
    price = float(input())
    if count % 3 == 0:
        price *= 1/2

    budget -= price
    if budget < 0:
        print("You don't have enough money!", f"\nYou need {abs(budget):.2f} leva!")
        exit()

    total += price
    items += 1

    product_name = input()

print(f"You bought {items} products for {total:.2f} leva.")