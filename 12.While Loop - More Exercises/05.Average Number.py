n = int(input())
sum_of_num = 0

for i in range(n):
    num = int(input())
    sum_of_num += num

print(f"{sum_of_num / n:.2f}")