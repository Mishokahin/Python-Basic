import math
tennis_rackets_price = float(input())
tennis_rackets_quantity = int(input())
shoes_quantity = int(input())

tennis_rackets_total = tennis_rackets_price * tennis_rackets_quantity
shoes_total = (tennis_rackets_price / 6) * shoes_quantity
additional_equipment = (tennis_rackets_total + shoes_total) * 0.2

equipment_total = tennis_rackets_total + shoes_total + additional_equipment

djokovic_portion = math.floor(equipment_total/8)
sponsor_portion = math.ceil(equipment_total * 7/8)

print(f"Price to be paid by Djokovic {djokovic_portion}")
print(f"Price to be paid by sponsors {sponsor_portion}")