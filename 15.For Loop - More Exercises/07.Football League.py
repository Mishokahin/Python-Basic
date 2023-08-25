sector_map = {"A": 0, "B": 0, "V": 0, "G": 0}
capacity = int(input())
fan_count = int(input())

for fan in range(fan_count):
    sector = input()
    if sector in sector_map:
        sector_map[sector] += 1

a_sector_percent = (sector_map["A"]/fan_count) * 100
b_sector_percent = (sector_map["B"]/fan_count) * 100
v_sector_percent = (sector_map["V"]/fan_count) * 100
g_sector_percent = (sector_map["G"]/fan_count) * 100
occupancy_percent = (fan_count/capacity) * 100

print(f"{a_sector_percent:.2f}%")
print(f"{b_sector_percent:.2f}%")
print(f"{v_sector_percent:.2f}%")
print(f"{g_sector_percent:.2f}%")
print(f"{occupancy_percent:.2f}%")