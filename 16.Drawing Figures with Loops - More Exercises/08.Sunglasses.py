import math
n = int(input())
for i in range(1, n+1):
    if i == 1 or i == n:
        print(((2*n) * "*") + (n * " ") + ((2*n) * "*"))
    elif i == math.ceil(n/2):
        print(("*" + ((2*n-2) * "/") + "*" + (n * "|") + "*" + ((2*n-2) * "/") + "*"))
    else:
        print(("*" + ((2 * n - 2) * "/") + "*" + (n * " ") + "*" + ((2 * n - 2) * "/") + "*"))