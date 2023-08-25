actor_name = input()
starting_points = float(input())
jury_members = int(input())

total_points = starting_points

for member in range(jury_members):
    member_name = input()
    points_given = float(input())
    total_points += (((len(member_name) * points_given)/2))

    if total_points >= 1250.5:
        break

if total_points >= 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
else:
    needed_score = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")