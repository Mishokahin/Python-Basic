import math
days = int(input())
food_left = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

food_needed = (days * first_deer_food) + (days * second_deer_food) + (days * third_deer_food)

if food_left >= food_needed:
    food_surplus = math.floor(food_left - food_needed)
    print(f"{food_surplus} kilos of food left.")
else:
    food_deficit = math.ceil(food_needed - food_left)
    print(f"{food_deficit} more kilos of food are needed.")