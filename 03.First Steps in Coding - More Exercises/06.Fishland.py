price_kg_mackerel = float(input())
price_kg_sprinkle = float(input())
kg_bonito = float(input())
kg_safrid = float(input())
kg_mussels = float(input())

price_bonito = price_kg_mackerel * (1 + 0.6)
price_safrid = price_kg_sprinkle * (1 + 0.8)
price_mussels = 7.5

bonito_total = price_bonito * kg_bonito
safrid_total = price_safrid * kg_safrid
mussels_total = price_mussels * kg_mussels

print(f"{bonito_total + safrid_total + mussels_total:.2f}")