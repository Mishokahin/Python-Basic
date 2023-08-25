budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_additional_expenses = int(input())

if nights > 7:
    price_per_night *= (1 - 0.05)

price_accommodation = nights * price_per_night
additional_expenses = (budget * percent_additional_expenses) / 100

total = price_accommodation + additional_expenses

if budget >= total:
    money_left = budget - total
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")

else:
    money_needed = total - budget
    print(f"{money_needed:.2f} leva needed.")