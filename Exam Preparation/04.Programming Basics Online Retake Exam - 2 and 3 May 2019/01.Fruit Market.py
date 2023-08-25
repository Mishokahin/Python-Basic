price_strawberry = float(input())
kilos_bananas = float(input())
kilos_oranges = float(input())
kilos_raspberry = float(input())
kilos_strawberry = float(input())

total_raspberry = kilos_raspberry * (price_strawberry/2)
total_bananas = kilos_bananas * ((price_strawberry/2) * (1 - 0.8))
total_oranges = kilos_oranges * ((price_strawberry/2) * (1 - 0.4))
total_strawberry = kilos_strawberry * price_strawberry

total = total_strawberry + total_bananas + total_oranges + total_raspberry

print(f"{total:.2f}")