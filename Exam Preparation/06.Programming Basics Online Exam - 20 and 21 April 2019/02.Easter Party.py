import sys
inputs = [int(input()), float(input()), float(input())]
discount = {range(10, 16): 0.15, range(16, 21): 0.20, range(21, sys.maxsize): 0.25}

for key in discount:
    if inputs[0] in key:
        inputs[1] *= (1 - discount[key])
total = [(inputs[0] * inputs[1]) + (inputs[2] * 0.1)]

if sum(total) <= inputs[2]:
    print(f"It is party time! {inputs[2] - sum(total):.2f} leva left.")

else:
    print(f"No party! {sum(total) - inputs[2]:.2f} leva needed.")