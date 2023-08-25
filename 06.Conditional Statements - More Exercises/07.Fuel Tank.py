fuel_types = ["Diesel", "Gasoline", "Gas"]

fuel = input()
fuel_quantity = int(input())

if fuel in fuel_types:
    if fuel_quantity >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")

else:
    print("Invalid fuel!")