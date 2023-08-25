import math
series_name = input()
seasons_count = int(input())
episodes_count = int(input())
no_ads_length = int(input())
with_ads_length = no_ads_length * (1 + 0.2)
specials_length = seasons_count * 10
total_time = math.floor((with_ads_length * episodes_count * seasons_count) + specials_length)

print(f"Total time needed to watch the {series_name} series is {total_time} minutes.")