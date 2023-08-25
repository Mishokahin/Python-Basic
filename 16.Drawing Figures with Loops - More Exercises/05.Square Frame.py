n = int(input())
for i in range(1, n+1):
    if i == 1 or i == n:
        print(f"+ " + str("- " * (n-2)) + "+")
    else:
        print("| " + str("- " * (n - 2)) + "|")