n = int(input())
nums = [int(input()) for i in range(n)]
p1 = [x for x in nums if x % 2 == 0]
p2 = [x for x in nums if x % 3 == 0]
p3 = [x for x in nums if x % 4 == 0]

print(f"{(len(p1)/n)*100:.2f}%", f"\n{(len(p2)/n)*100:.2f}%", f"\n{(len(p3)/n)*100:.2f}%")
