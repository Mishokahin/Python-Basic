inputs = {"total days": int(input()), "total food": float(input())}
food_eaten = {i: [int(input()), int(input())] for i in range(1, inputs["total days"]+1)}
dog_food = [food_eaten[i][0] for i in range(1, inputs["total days"]+1)]
cat_food = [food_eaten[i][1] for i in range(1, inputs["total days"]+1)]
bonus = [sum(food_eaten[i]) * 0.1 for i in range(1, inputs["total days"]+1) if i % 3 == 0]
total_eaten = sum(cat_food) + sum(dog_food)
print(f"Total eaten biscuits: {round(sum(bonus))}gr.")
print(f"{(total_eaten / inputs['total food']) * 100:.2f}% of the food has been eaten.")
print(f"{(sum(dog_food)/total_eaten) * 100:.2f}% eaten from the dog.")
print(f"{(sum(cat_food)/total_eaten) * 100:.2f}% eaten from the cat.")