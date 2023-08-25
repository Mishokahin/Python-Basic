from math import pi

shape = input()

if shape == "square":
    i = float(input())
    print(f"{i*i:.3f}")
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif shape == "circle":
    r = float(input())
    print(f"{pi * (r*r):.3f}")
elif shape == "triangle":
    h = float(input())
    b = float(input())
    print(f"{(h * b)/2:.3f}")