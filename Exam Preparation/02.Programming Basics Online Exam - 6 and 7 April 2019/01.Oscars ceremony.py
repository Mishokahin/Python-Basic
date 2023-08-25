rent = int(input())
statues = rent * (1 - 0.3)
catering = statues * (1 - 0.15)
sound = catering / 2
total = rent + statues + catering + sound

print(f"{total:.2f}")