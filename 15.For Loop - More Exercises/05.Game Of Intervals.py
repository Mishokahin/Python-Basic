import sys
percentage_map = {"to_nine" : 0,
                  "to_nineteen": 0,
                  "to_twentynine": 0,
                  "to_thirtynine": 0,
                  "to_fifty": 0,
                  "invalid": 0
                  }

number_of_tries = int(input())
points = 0
percent = ""

for i in range(number_of_tries):
    number = int(input())
    point_map = {range(-sys.maxsize, 0): ["invalid", -1 * (points / 2)],
                 range(0, 10): ["to_nine", number * 0.2],
                 range(10, 20): ["to_nineteen", number * 0.3],
                 range(20, 30): ["to_twentynine", number * 0.4],
                 range(30, 40): ["to_thirtynine", 50],
                 range(40, 51): ["to_fifty", 100],
                 range(51, sys.maxsize): ["invalid", -1 * (points / 2)]
                 }
    for key in point_map:
        if number in key:
            percent = point_map[key][0]
            points += point_map[key][1]

    if percent in percentage_map:
        percentage_map[percent] += 1

numbers_to_nine = (percentage_map["to_nine"]/number_of_tries) * 100
numbers_to_nineteen = (percentage_map["to_nineteen"]/number_of_tries) * 100
numbers_to_twentynine = (percentage_map["to_twentynine"]/number_of_tries) * 100
numbers_to_thirtynine = (percentage_map["to_thirtynine"]/number_of_tries) * 100
numbers_to_fifty = (percentage_map["to_fifty"]/number_of_tries) * 100
invalid_numbers = (percentage_map["invalid"]/number_of_tries) * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {numbers_to_nine:.2f}%")
print(f"From 10 to 19: {numbers_to_nineteen:.2f}%")
print(f"From 20 to 29: {numbers_to_twentynine:.2f}%")
print(f"From 30 to 39: {numbers_to_thirtynine:.2f}%")
print(f"From 40 to 50: {numbers_to_fifty:.2f}%")
print(f"Invalid numbers: {invalid_numbers:.2f}%")