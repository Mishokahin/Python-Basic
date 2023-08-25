male_count = int(input())
female_count = int(input())
tables = int(input())

couples = [f"({i} <-> {j})"
           for i in range(1, male_count+1)
           for j in range(1, female_count+1)]

print(*couples[:tables])