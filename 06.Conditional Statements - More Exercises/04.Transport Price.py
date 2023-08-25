distance = int(input())
time_of_day = input()

if distance >= 100:
    print(f"{distance * 0.06:.2f}")

elif 100 > distance >= 20:
    print(f"{distance * 0.09:.2f}")

else:
    if time_of_day == "day":
        print(f"{0.70 + (distance * 0.79):.2f}")
    elif time_of_day == "night":
        print(f"{0.70 + (distance * 0.9):.2f}")