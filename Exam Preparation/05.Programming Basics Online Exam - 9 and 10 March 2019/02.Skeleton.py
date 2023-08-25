minutes = int(input())
seconds = int(input())
distance = float(input())
seconds_per_hundred_m = int(input())

control_time_total = (minutes * 60) + seconds
time_penalty = (distance/120) * 2.5
marin_time = (distance/100) * seconds_per_hundred_m - time_penalty

time_difference = marin_time - control_time_total

if marin_time <= control_time_total:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")

else:
    print(f"No, Marin failed! He was {time_difference:.3f} second slower.")