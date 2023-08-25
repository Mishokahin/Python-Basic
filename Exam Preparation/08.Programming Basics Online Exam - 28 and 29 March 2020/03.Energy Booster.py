prices = {"Watermelon": {"small": 56 * 2, "big": 28.70 * 5},
          "Mango": {"small": 36.66 * 2, "big": 19.60 * 5},
          "Pineapple": {"small": 42.10 * 2, "big": 24.80 * 5},
          "Raspberry": {"small": 20 * 2, "big": 15.20 * 5}
          }

inputs = [input(), input(), int(input())]
price = prices[inputs[0]][inputs[1]] * inputs[2]

if 400 <= price <= 1000:
    print(f"{price * 0.85:.2f} lv.")

elif price > 1000:
    print(f"{price * 0.5:.2f} lv.")

else:
    print(f"{price:.2f} lv.")