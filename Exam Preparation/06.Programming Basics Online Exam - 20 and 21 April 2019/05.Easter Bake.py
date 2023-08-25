import math
bread_count = int(input())
ingredient = [[int(input()), int(input())] for i in range(bread_count)]
sugar = [ingredient[x][0] for x in range(len(ingredient))]
flour = [ingredient[x][1] for x in range(len(ingredient))]

print(f"Sugar: {math.ceil(sum(sugar)/950)}")
print(f"Flour: {math.ceil(sum(flour)/750)}")
print(f"Max used flour is {max(flour)} grams, max used sugar is {max(sugar)} grams.")