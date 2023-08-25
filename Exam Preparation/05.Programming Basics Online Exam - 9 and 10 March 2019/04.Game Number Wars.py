p1_name = input()
p2_name = input()
p1_score = 0
p2_score = 0

p1_card = input()

while p1_card != "End of game":
    p2_card = input()

    if int(p1_card) == int(p2_card):
        p1_card = int(input())
        p2_card = int(input())
        if p1_card > p2_card:
            print("Number wars!", f"\n{p1_name} is winner with {p1_score} points")
        else:
            print("Number wars!", f"\n{p2_name} is winner with {p2_score} points")
        exit()
    elif int(p1_card) > int(p2_card):
        p1_score += int(p1_card) - int(p2_card)

    elif int(p1_card) < int(p2_card):
        p2_score += int(p2_card) - int(p1_card)

    p1_card = input()

print(f"{p1_name} has {p1_score} points", f"\n{p2_name} has {p2_score} points")