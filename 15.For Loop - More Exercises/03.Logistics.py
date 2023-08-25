import sys
vehicle_type = {range(-sys.maxsize, 4): "by_bus",
                range(4, 12): "by_truck",
                range(12, sys.maxsize): "by_train"
                }
loads = {"by_bus": [0, 200],
         "by_truck": [0, 175],
         "by_train": [0, 120]
         }

number_of_loads = int(input())
load_type = ""


for load in range(number_of_loads):
    tons_load = int(input())
    for key in vehicle_type:
        if tons_load in key:
           load_type = vehicle_type[key]

    if load_type in loads:
        loads[load_type][0] += tons_load


total_tons_loads = loads["by_bus"][0] + loads["by_truck"][0] + loads["by_train"][0]
average_price_ton = ((loads["by_bus"][0] * loads["by_bus"][1]) + (loads["by_truck"][0] * loads["by_truck"][1]) +
                     (loads["by_train"][0] * loads["by_train"][1])) / total_tons_loads
percentage_by_bus = (loads["by_bus"][0]/total_tons_loads) * 100
percentage_by_truck = (loads["by_truck"][0]/total_tons_loads) * 100
percentage_by_train = (loads["by_train"][0]/total_tons_loads) * 100

print(f"{average_price_ton:.2f}")
print(f"{percentage_by_bus:.2f}%")
print(f"{percentage_by_truck:.2f}%")
print(f"{percentage_by_train:.2f}%")