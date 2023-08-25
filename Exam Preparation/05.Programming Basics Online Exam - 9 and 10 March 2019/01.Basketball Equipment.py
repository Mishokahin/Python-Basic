fee = int(input())
shoes = fee * (1 - 0.4)
clothes = shoes * (1 - 0.2)
ball = clothes / 4
accessories = ball / 5

total = fee + shoes + clothes + ball + accessories

print(f"{total:.2f}")