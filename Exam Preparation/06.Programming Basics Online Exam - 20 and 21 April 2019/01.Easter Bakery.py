inputs = [float(input()), float(input()), float(input()), float(input()), float(input())]
prices = [inputs[0], inputs[0] * 0.75, inputs[0] * 1.1, (inputs[0] * 0.75) * 0.2]
total = [inputs[1]*prices[0], inputs[2]*prices[1], inputs[3]*prices[2], inputs[4]*prices[3]]

print(f"{sum(total):.2f}")