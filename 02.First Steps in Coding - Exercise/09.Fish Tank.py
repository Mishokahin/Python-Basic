length = int(input())
width = int(input())
height = int(input())
occupiedPercentage = float(input())

print(((length * width * height) / 1000) * (1 - (occupiedPercentage/100)))
