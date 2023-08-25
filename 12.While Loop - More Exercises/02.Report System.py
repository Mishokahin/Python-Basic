money_needed = input()
payment = input()
counter = 0
cs_sum = 0
cc_sum = 0
cs_payments = 0
cc_payments = 0

total = 0

while payment != "End":
    counter += 1
    if counter % 2 == 0:
        if float(payment) < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cc_sum += float(payment)
            cc_payments += 1
    else:
        if float(payment) > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cs_sum += float(payment)
            cs_payments += 1

    total = cs_sum + cc_sum

    if total >= float(money_needed):
        break

    payment = input()

if total >= float(money_needed):
    average_cs = cs_sum / cs_payments
    average_cc = cc_sum / cc_payments
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")

else:
    print("Failed to collect required money for charity.")