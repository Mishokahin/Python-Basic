import sys
ticket_category = {"VIP": 499.99, "Normal": 249.99}
transportation = {range(1, 5): 0.75, range(5, 10): 0.6, range(10, 25): 0.5, range(25, 50): 0.4,
                  range(50, sys.maxsize): 0.25}

budget = float(input())
ticket = input()
people = int(input())

if ticket in ticket_category:
    ticket_price = people * ticket_category[ticket]

for key in transportation:
    if people in key:
        transportation_price = budget * transportation[key]
        break

total = ticket_price + transportation_price

if total <= budget:
    money_left = budget - total
    print(f"Yes! You have {money_left:.2f} leva left.")

else:
    money_needed = total - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")