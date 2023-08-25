import math

days = int(input())
pet_food = int(input())
kg_dog_food = float(input())
kg_cat_food = float(input())
kg_turtle_food = float(input()) / 1000

food_needed = (kg_turtle_food * days) + (kg_cat_food * days) + (kg_dog_food * days)

if food_needed <= pet_food:
    food_left = math.floor(pet_food - food_needed)
    print(f"{food_left} kilos of food left.")

else:
    more_food_needed = math.ceil(food_needed - pet_food)
    print(f"{more_food_needed} more kilos of food are needed.")