number_of_groups = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0


for n in range(number_of_groups):
    climbers = int(input())
    if climbers <= 5:
        musala += climbers
    elif 6 <= climbers <= 12:
        mont_blanc += climbers
    elif 13 <= climbers <= 25:
        kilimanjaro += climbers
    elif 26 <= climbers <= 40:
        k2 += climbers
    elif 41 <= climbers:
        everest += climbers

total_climbers = musala + mont_blanc + kilimanjaro + k2 + everest

print(f"{(musala / total_climbers) * 100:.2f}%")
print(f"{(mont_blanc / total_climbers) * 100:.2f}%")
print(f"{(kilimanjaro / total_climbers) * 100:.2f}%")
print(f"{(k2 / total_climbers) * 100:.2f}%")
print(f"{(everest / total_climbers) * 100:.2f}%")