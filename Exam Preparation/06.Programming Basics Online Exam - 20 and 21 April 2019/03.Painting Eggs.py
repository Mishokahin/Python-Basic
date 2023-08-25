inputs = [input(), input(), int(input())]
prices = {"Large": {"Red": 16, "Green": 12, "Yellow": 9},
          "Medium": {"Red": 13, "Green": 9, "Yellow": 7},
          "Small": {"Red": 9, "Green": 8, "Yellow": 5}
          }
total = (prices[inputs[0]][str(inputs[1])]) * inputs[2] * (1 - 0.35)

print(f"{total:.2f} leva.")