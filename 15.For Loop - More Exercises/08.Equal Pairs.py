pair_count = int(input())
previous_pair = int(input()) + int(input())
max_diff = 0

for i in range(pair_count -1):
    current_pair = int(input()) + int(input())

    if abs(previous_pair - current_pair) > max_diff:
        max_diff = abs(previous_pair - current_pair)

    previous_pair = current_pair

if max_diff == 0:
    print(f"Yes, value={previous_pair}")
else:
    print(f"No, maxdiff={max_diff}")