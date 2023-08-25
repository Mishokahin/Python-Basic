budget = float(input())
gpuQuantity = int(input())
cpuQuantity = int(input())
ramQuantity = int(input())

gpuPrice = gpuQuantity * 250
cpuPrice = cpuQuantity * (gpuPrice * 0.35)
ramPrice = ramQuantity * (gpuPrice * 0.10)

totalPrice = gpuPrice + cpuPrice + ramPrice

if gpuQuantity > cpuQuantity:
    totalPrice -= totalPrice * 0.15

if totalPrice <= budget:
    print(f"You have {budget - totalPrice:.2f} leva left!")

else:
    print(f"Not enough money! You need {totalPrice - budget:.2f} leva more!")