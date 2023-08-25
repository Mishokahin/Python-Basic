inputs = [input(), input(), int(input())]
prices = {"France": {"21-23": 30, "24-27": 35, "28-31": 40},
          "Italy": {"21-23": 28, "24-27": 32, "28-31": 39},
          "Germany": {"21-23": 32, "24-27": 37, "28-31": 43}
          }
total = prices[inputs[0]][str(inputs[1])] * inputs[2]

print(f"Easter trip to {inputs[0]} : {total:.2f} leva.")