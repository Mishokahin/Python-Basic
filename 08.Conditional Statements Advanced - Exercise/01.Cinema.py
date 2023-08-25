screeningPrices = {"premiere": 12, "normal": 7.5, "discount": 5}

screeningType = input().lower()
rows = int(input())
columns = int(input())

print(f"{screeningPrices[screeningType] * (rows * columns):.2f} leva")