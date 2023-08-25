time_per_walk = int(input())
walks_count = int(input())
daily_calories = int(input())

burned_calories = time_per_walk * walks_count * 5

if burned_calories >= daily_calories/2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {int(burned_calories)}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {int(burned_calories)}.")