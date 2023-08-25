days_count = int(input())
hours_count = int(input())
daily_total = 0
total = 0

for day in range(1, days_count+1):
    daily_total = 0
    for hour in range(1, hours_count+1):
        if day % 2 == 0 and hour % 2 != 0:
            daily_total += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            daily_total += 1.25
        else:
            daily_total += 1
    total += daily_total
    print(f"Day: {day} - {daily_total:.2f} leva")
print(f"Total: {total:.2f} leva")