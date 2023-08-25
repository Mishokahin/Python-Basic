number_one = int(input())
number_two = int(input())
number_three = int(input())

prime_numbers = [2, 3, 5, 7]

pin_codes = [f"{i} {j} {k}"
             for i in range(1, number_one + 1)
             for j in range(1, number_two+1)
             for k in range(1, number_three+1)
             if i % 2 == 0 and j in prime_numbers and k % 2 == 0]

print(*pin_codes, sep="\n")