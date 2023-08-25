total_eggs = int(input())
sold_eggs = 0
command = input()

while command != "Close":
    eggs = int(input())
    if command == "Buy":
        if eggs > total_eggs:
            print("Not enough eggs in store!", f"\nYou can buy only {total_eggs}.")
            exit()
        else:
            total_eggs -= eggs
            sold_eggs += eggs
    else:
        total_eggs += eggs

    command = input()

print("Store is closed!", f"\n{sold_eggs} eggs sold.")