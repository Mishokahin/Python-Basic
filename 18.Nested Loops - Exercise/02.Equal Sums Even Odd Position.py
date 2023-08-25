first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
    num_to_str = str(num)
    sum_even = 0
    sum_odd = 0

    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    if sum_even == sum_odd:
        print(num, end=" ")