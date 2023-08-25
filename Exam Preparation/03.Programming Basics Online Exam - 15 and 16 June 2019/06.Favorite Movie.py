import string
name = input()
score = 0
highest_score_name = ""
count = 0

while name != "STOP":
    count += 1
    current_score = 0
    for i in name:
        if i in string.ascii_uppercase:
            current_score += ord(i) - len(name)
        elif i in string.ascii_lowercase:
            current_score += ord(i) - (len(name) * 2)
        else:
            current_score += ord(i)

    if current_score > score:
        score = current_score
        highest_score_name = name

    if count == 7:
        print("The limit is reached.",
              f"\nThe best movie for you is {highest_score_name} with {score} ASCII sum.")
        exit()

    name = input()

print(f"The best movie for you is {highest_score_name} with {score} ASCII sum.")