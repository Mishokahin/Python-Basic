destination = input()
money_saved = 0

while destination != "End":
    money_needed = float(input())
    while money_saved <= money_needed:
        money = float(input())
        money_saved += money
        if money_saved >= money_needed:
            print(f"Going to {destination}!")
            break
    money_saved = 0
    destination = input()