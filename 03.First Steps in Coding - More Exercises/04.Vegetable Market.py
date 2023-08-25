price_kg_veg = float(input())
price_kg_fruit = float(input())
kilos_veg = int(input())
kilos_fruit = int(input())
euro = 1.94

total_price = (price_kg_veg * kilos_veg) + (price_kg_fruit * kilos_fruit)

print(f"{total_price / euro:.2f}")