inputs = [int(input()), int(input())]

command = input()

while command != "End":
    if command == "one":
        inputs[1] -= 1
    else:
        inputs[0] -= 1

    if inputs[0] == 0 or inputs[1] == 0:
        if inputs[0] == 0:
            print(f"Player one is out of eggs. Player two has {inputs[1]} eggs left.")
        else:
            print(f"Player two is out of eggs. Player one has {inputs[0]} eggs left.")
        exit()

    command = input()

print(f"Player one has {inputs[0]} eggs left.")
print(f"Player two has {inputs[1]} eggs left.")