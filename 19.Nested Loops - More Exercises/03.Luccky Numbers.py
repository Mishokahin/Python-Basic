n = int(input())

lucky_numbers = [f"{i}{j}{k}{l}"
                 for i in range(1, 10)
                 for j in range(1, 10)
                 for k in range(1, 10)
                 for l in range(1, 10)
                 if i + j == k + l and n % (i + j) == 0]

print(*lucky_numbers)