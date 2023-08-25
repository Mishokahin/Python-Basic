import sys
min_number = sys.maxsize
number = input()

while number != "Stop":
    num = int(number)

    if num < min_number:
        min_number = num

    number = input()

print(min_number)