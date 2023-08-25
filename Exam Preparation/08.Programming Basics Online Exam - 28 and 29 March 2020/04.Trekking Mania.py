number_of_groups = int(input())
people = [int(input()) for i in range(number_of_groups)]
musala = [x for x in people if x <= 5]
montblanc = [x for x in people if 6 <= x <= 12]
kilimanjaro = [x for x in people if 13 <= x <= 25]
k2 = [x for x in people if 26 <= x <= 40]
everest = [x for x in people if 41 <= x]

print(f"{(sum(musala)/sum(people))*100:.2f}%")
print(f"{(sum(montblanc)/sum(people))*100:.2f}%")
print(f"{(sum(kilimanjaro)/sum(people))*100:.2f}%")
print(f"{(sum(k2)/sum(people))*100:.2f}%")
print(f"{(sum(everest)/sum(people))*100:.2f}%")