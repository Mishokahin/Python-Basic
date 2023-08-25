penalty_table = {"Facebook": 150, "Instagram": 100, "Reddit": 50}
tabs_open = int(input())
salary = int(input())

for tab in range(tabs_open):
    tab = input()
    if tab in penalty_table:
        salary -= penalty_table[tab]
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(salary)