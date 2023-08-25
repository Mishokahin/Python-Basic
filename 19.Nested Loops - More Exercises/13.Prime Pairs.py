first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

prime_numbers = [x for x in range(10, 100) if all(x % y for y in range(2, x))]

prime_pairs = [f"{i}{j}"
               for i in range(first_pair_start, (first_pair_start+first_pair_diff)+1)
               for j in range(second_pair_start, (second_pair_start+second_pair_diff)+1)
               if i in prime_numbers and j in prime_numbers
               ]

print(*prime_pairs, sep="\n")
