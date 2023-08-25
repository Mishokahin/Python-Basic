n = int(input())
current_n = 1

for row in range(1, n+1):
    for col in range(1, row + 1):
        if current_n > n:
            exit()
        print(f"{current_n} ", end ="")
        current_n += 1
    print()