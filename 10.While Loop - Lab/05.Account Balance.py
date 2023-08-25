value = input()
balance = 0

while value != "NoMoreMoney":
    amount_added = float(value)
    if amount_added < 0:
        print("Invalid operation!")
        break

    balance += amount_added
    print(f"Increase: {amount_added:.2f}")
    value = input()

print(f"Total: {balance:.2f}")