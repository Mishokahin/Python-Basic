age = 18
inheritance = float(input())
year_to_live_to = int(input())

for i in range(1800, year_to_live_to+1):
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= (12000 + (age * 50))
    age += 1

if inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")

else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")