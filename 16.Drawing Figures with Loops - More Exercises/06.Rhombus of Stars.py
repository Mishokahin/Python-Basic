n = int(input())
for row in range(1, n + 1):
    if row == 1:
        print(" " * (n - row) + "*" * row)
    else:
        print(" " * (n - row) + "* " * row)
for row in range(n-1, 0, -1):
    if row == 0:
        print(" " * (n - row) + "*" * row)
    else:
        print(" " * (n - row) + "* " * row)