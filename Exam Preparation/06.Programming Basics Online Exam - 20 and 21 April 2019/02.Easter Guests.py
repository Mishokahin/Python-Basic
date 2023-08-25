import math
inputs = [int(input()), int(input())]
products = [math.ceil(inputs[0]/3), (inputs[0]*2)]
total = [(products[0] * 4) + (products[1] * 0.45)]

if sum(total) <= inputs[1]:
    print(f"Lyubo bought {products[0]} Easter bread and {products[1]} eggs.")
    print(f"He has {inputs[1] - sum(total):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {sum(total) - inputs[1]:.2f} lv. more.")