a1 = int(input())
a2 = int(input())
n = int(input())

tickets = [f"{chr(i)}-{j}{k}{i}"
           for i in range(a1, a2)
           for j in range(1, n)
           for k in range(1, int((n/2)))
           if i % 2 != 0 and (i + j + k) % 2 != 0
           ]

print(*tickets, sep="\n")