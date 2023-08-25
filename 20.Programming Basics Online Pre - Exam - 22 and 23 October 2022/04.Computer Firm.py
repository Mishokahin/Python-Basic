ratings = {2: 0, 3: 0.5, 4: 0.7, 5: 0.85, 6: 1}
n = int(input())
sales = [input() for i in range(n)]
total_sales = 0
total_rating = 0
for i in sales:
    pc_count = int(i[:2])
    rating = ratings[int(i[2])]
    total_rating += int(i[2])
    total_sales += pc_count * rating

print(f"{total_sales:.2f}")
print(f"{total_rating / n:.2f}")