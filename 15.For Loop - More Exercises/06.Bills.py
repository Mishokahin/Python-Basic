months = int(input())
water = 0
electricity = 0
other = 0
internet = 0

for i in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15
    other += (electricity_bill + 20 + 15) * (1 + 0.2)

average = (water + electricity + other + internet) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")