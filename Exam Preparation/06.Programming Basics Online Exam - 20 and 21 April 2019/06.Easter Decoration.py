prices = {"basket": 1.50, "wreath": 3.80, "chocolate bunny": 7}
customer_count = int(input())
total = 0

for i in range(customer_count):
    item_count = 0
    current_total = 0
    purchase = input()
    while purchase != "Finish":
        current_total += prices[str(purchase)]
        item_count += 1
        purchase = input()

    if item_count % 2 == 0:
        current_total *= (1 - 0.2)

    print(f"You purchased {item_count} items for {current_total:.2f} leva.")

    total += current_total

print(f"Average bill per client is: {total/customer_count:.2f} leva.")