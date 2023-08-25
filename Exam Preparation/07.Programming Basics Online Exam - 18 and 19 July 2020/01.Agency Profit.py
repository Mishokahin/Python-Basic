inputs = [input(), int(input()), int(input()), float(input()), float(input())]
prices = [inputs[3] + inputs[4], (inputs[3] * 0.3) + inputs[4]]
profit = ((inputs[1] * prices[0]) + (inputs[2] * prices[1])) * 0.2

print(f"The profit of your agency from {inputs[0]} tickets is {profit:.2f} lv.")