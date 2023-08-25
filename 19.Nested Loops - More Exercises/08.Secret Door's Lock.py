prime_numbers = [2, 3, 5, 7]
hundreds = int(input())
tens = int(input())
ones = int(input())

combinations = [f"{i} {j} {k}"
                for i in range(1, hundreds+1)
                for j in range(1, tens+1)
                for k in range(1, ones+1)
                if i % 2 == 0 and j in prime_numbers and k % 2 == 0]

print(*combinations, sep="\n")