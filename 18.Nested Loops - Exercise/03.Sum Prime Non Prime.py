command = input()
sum_prime = 0
sum_non_prime = 0

while command != "stop":
    num = int(command)
    is_prime = True

    if num < 0:
        num = 0
        print("Number is negative.")

    elif num == 1:
        is_prime = False

    else:
        for i in range(2, num + 1):
            if num % i == 0 and i != num:
                is_prime = False
                break

    if is_prime:
        sum_prime += num

    elif not is_prime:
        sum_non_prime += num

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")

