vouchers = int(input())
ticket_count = 0
misc_count = 0
command = input()

while command != "End":
    current_total = 0
    if len(command) > 8:
        current_total = ord(command[0]) + ord(command[1])
    else:
        current_total = ord(command[0])

    if current_total > vouchers:
        break
    else:
        if len(command) > 8:
            ticket_count += 1
        else:
            misc_count += 1

    vouchers -= current_total

    command = input()

print(f"{ticket_count}", f"\n{misc_count}")