weather = float(input())

if 35 >= weather >= 26:
    print("Hot")
elif 25.9 >= weather >= 20.1:
    print("Warm")
elif 20.00 >= weather >= 15.00:
    print("Mild")
elif 14.9 >= weather >= 12.00:
    print("Cool")
elif 11.9 >= weather >= 5.00:
    print("Cold")
else:
    print("unknown")