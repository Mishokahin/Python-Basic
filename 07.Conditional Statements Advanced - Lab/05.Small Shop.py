prices = {
    "sofia": {
        "coffee": 0.5,
        "water": 0.8,
        "beer": 1.2,
        "sweets": 1.45,
        "peanuts": 1.6
    },
    "plovdiv": {
        "coffee": 0.4,
        "water": 0.7,
        "beer": 1.15,
        "sweets": 1.30,
        "peanuts": 1.50
    },
    "varna": {
        "coffee": 0.45,
        "water": 0.7,
        "beer": 1.10,
        "sweets": 1.35,
        "peanuts": 1.55
    }
}

product = input().lower()
city = input().lower()
quantity = float(input())
price = 0

if city in prices:
    if product in prices[city]:
        price = prices[city][product] * quantity

print(price)