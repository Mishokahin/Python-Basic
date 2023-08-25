import math
inputs = (float(input()), float(input()), float(input()))
total_time = sum([inputs[1]*inputs[2], math.floor(inputs[1]/50) * 30])
if total_time >= inputs[0]:
    print(f"No! He was {total_time - inputs[0]:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")