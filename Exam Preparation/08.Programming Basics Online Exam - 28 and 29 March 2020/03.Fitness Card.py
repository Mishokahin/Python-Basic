prices = {"m": {"Gym": 42, "Boxing": 41, "Yoga": 45, "Zumba": 34, "Dances": 51, "Pilates": 39},
          "f": {"Gym": 35, "Boxing": 37, "Yoga": 42, "Zumba": 341, "Dances": 53, "Pilates": 37}
          }

inputs = [float(input()), input(), int(input()), input()]

price = prices[str(inputs[1])][str(inputs[3])]

if inputs[2] <= 19:
    price *= 0.8

if price <= inputs[0]:
    print(f"You purchased a 1 month pass for {str(inputs[3])}.")

else:
    print(f"You don't have enough money! You need ${price - inputs[0]:.2f} more.")