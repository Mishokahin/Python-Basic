commissionLevels = {"sofia": {"l1": 0.05, "l2": 0.07, "l3": 0.08, "l4": 0.12},
                    "varna": {"l1": 0.045, "l2": 0.075, "l3": 0.10, "l4": 0.13},
                    "plovdiv": {"l1": 0.055, "l2": 0.08, "l3": 0.12, "l4": 0.145}}
city = input().lower()
sales = float(input())

if city in commissionLevels:
    if 0 <= sales <= 500:
        print(f"{sales * commissionLevels[city]['l1']:.2f}")
    elif 500 < sales <= 1000:
        print(f"{sales * commissionLevels[city]['l2']:.2f}")
    elif 1000 < sales <= 10000:
        print(f"{sales * commissionLevels[city]['l3']:.2f}")
    elif sales > 10000:
            print(f"{sales * commissionLevels[city]['l4']:.2f}")
    else:
        print("error")
else:
    print("error")