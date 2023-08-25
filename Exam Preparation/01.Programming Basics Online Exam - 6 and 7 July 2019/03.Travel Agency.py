price_and_discount = {"Bansko": {"withEquipment": [100, 0.1], "noEquipment": [80, 0.05]},
                      "Borovets": {"withEquipment": [100, 0.1], "noEquipment": [80, 0.05]},
                      "Varna": {"withBreakfast": [130, 0.12], "noBreakfast": [100, 0.07]},
                      "Burgas": {"withBreakfast": [130, 0.12], "noBreakfast": [100, 0.07]}
                      }
city = input()
package = input()
vip_card = input()
stay = int(input())
total = 0

if stay < 1:
    print("Days must be positive number!")

elif city in price_and_discount:
    if stay > 7:
        stay -= 1
    if package in price_and_discount[city]:
        if vip_card == "yes":
            total = (price_and_discount[city][package][0] * (1 - price_and_discount[city][package][1])) * stay
            print(f"The price is {total:.2f}lv! Have a nice time!")
        elif vip_card == "no":
            total = price_and_discount[city][package][0] * stay
            print(f"The price is {total:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

else:
    print("Invalid input!")