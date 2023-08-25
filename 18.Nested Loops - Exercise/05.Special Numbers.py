n = int(input())

for num in range(1111, 9999 + 1):
    my_list = [int(x) for x in str(num)]
    count = 0
    if my_list[0] == 0 or my_list[1] == 0 or my_list[2] == 0 or my_list[3] == 0:
        count = 0
    else:
        if n % my_list[0] == 0:
            count += 1
        if n % my_list[1] == 0:
            count += 1
        if n % my_list[2] == 0:
            count += 1
        if n % my_list[3] == 0:
            count += 1

    if count == 4:
        print(num, end=" ")