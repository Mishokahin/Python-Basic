head_count = int(input())
activity = [input() for x in range(head_count)]
back = [x for x in activity if x == "Back"]
chest = [x for x in activity if x == "Chest"]
legs = [x for x in activity if x == "Legs"]
abs = [x for x in activity if x == "Abs"]
protein_shake = [x for x in activity if x == "Protein shake"]
protein_bar = [x for x in activity if x == "Protein bar"]
workout_percent = ((len(back) + len(chest) + len(legs) + len(abs)) / head_count) * 100
protein_percent = ((len(protein_shake) + len(protein_bar)) / head_count) * 100

print(f"{len(back)} - back")
print(f"{len(chest)} - chest")
print(f"{len(legs)} - legs")
print(f"{len(abs)} - abs")
print(f"{len(protein_shake)} - protein shake")
print(f"{len(protein_bar)} - protein bar")
print(f"{workout_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")