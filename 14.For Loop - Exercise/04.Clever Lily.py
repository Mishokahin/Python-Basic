age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money_received = 0
toys_receive = 0
money_stolen = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money_received += 10 * (i/2)
        money_stolen += 1
    else:
        toys_receive += 1

toys_sold = toys_receive * toy_price
money_saved = (money_received + toys_sold) - money_stolen
diff = abs(money_saved - washing_machine_price)

if money_saved >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")