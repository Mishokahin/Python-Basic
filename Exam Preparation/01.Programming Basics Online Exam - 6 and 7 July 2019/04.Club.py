target_money = float(input())
total = 0
current_drink = 0
drink = input()

while drink != "Party!":
    drink_count = int(input())
    current_drink = len(drink) * drink_count
    if current_drink % 2 != 0:
        current_drink *= (1 - 0.25)
    total += current_drink
    if total >= target_money:
        print("Target acquired.")
        print(f"Club income - {total:.2f} leva.")
        exit()
    drink = input()

money_needed = target_money - total
print(f"We need {money_needed:.2f} leva more.")
print(f"Club income - {total:.2f} leva.")