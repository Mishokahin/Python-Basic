import sys
max_number = -sys.maxsize
number = input()

while number != "Stop":
    num = int(number)

    if num > max_number:
        max_number = num

    number = input()

print(max_number)