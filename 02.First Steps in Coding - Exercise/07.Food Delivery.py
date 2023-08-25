chickenMenu = int(input())
fishMenu = int(input())
vegetarianMenu = int(input())
deliveryFee = 2.5

totalMenus = (chickenMenu * 10.35) + (fishMenu * 12.40) + (vegetarianMenu * 8.15)
desert = totalMenus * 0.2

print(totalMenus + desert + deliveryFee)