money_needed = float(input())
money_on_hand = float(input())

days_passed = 0
days_spending = 0

while money_on_hand < money_needed and days_spending < 5:
    command = input()
    money = float(input())
    days_passed += 1
    if command == "save":
        money_on_hand += money
        days_spending = 0
    elif command == "spend":
        money_on_hand -= money
        days_spending += 1
        if money_on_hand < 0:
            money_on_hand = 0

if days_spending == 5:
    print(f"You can't save the money.")
    print(f"{days_passed}")

if money_on_hand >= money_needed:
    print(f"You saved the money for {days_passed} days.")