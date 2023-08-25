inputs = [int(input()), int(input()), float(input()), int(input())]
prices = [5.8, 7.2, 1.2]
sub_total = (inputs[0]*prices[0]) + (inputs[1]*prices[1]) + (inputs[2]*prices[2])
discount = inputs[3]/100
total = sub_total * (1 - discount)
print(f"{total:.3f}")