import math
n = int(input())
num = []
if n % 2 == 0:
    for i in range(2, n + 1, 2):
        num.append(i)
    for f in range(0, math.ceil(n / 2)):
        print((int(((n - num[f]) / 2)) * "-") + (int(num[f]) * "*") + (int(((n - num[f]) / 2)) * "-"))
    for f in range(int((n/2) + 1), n+1):
        print("|" + ((n-2) * "*") + "|")

else:
    for i in range(1, n + 1, 2):
        num.append(i)
    for f in range(0, math.ceil((n / 2))):
        print((int(((n - num[f]) / 2)) * "-") + (int(num[f]) * "*") + (int(((n - num[f]) / 2)) * "-"))
    for f in range(int((n / 2)), n-1):
        print("|" + ((n - 2) * "*") + "|")