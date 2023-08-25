days = int(input())
typeOfAccommodation = input()
review = input()

price = 0

if typeOfAccommodation == "room for one person":
    price = (days - 1) * 18

elif typeOfAccommodation == "apartment":
    price = (days - 1) * 25
    if (days - 1) < 10:
        price -= price * 0.3
    elif 10 <= (days - 1) <= 15:
        price -= price * 0.35
    elif 15 < (days - 1):
        price -= price * 0.5

elif typeOfAccommodation == "president apartment":
    price = (days - 1) * 35
    if (days - 1) < 10:
        price -= price * 0.1
    elif 10 <= (days - 1) <= 15:
        price -= price * 0.15
    elif 15 < (days - 1):
        price -= price * 0.2

if review == "positive":
    price += price * 0.25

elif review == "negative":
    price -= price * 0.1

print(f"{round(price, 2):.2f}")