n = int(input())

presentation = input()
grade_count = 0
final_grade = 0

while presentation != "Finish":
    current_grade = 0
    for i in range(n):
        grade = float(input())
        current_grade += grade
        final_grade += grade
        grade_count += 1

    print(f"{presentation} - {current_grade/n:.2f}.")
    presentation = input()

print(f"Student's final assessment is {final_grade / grade_count:.2f}.")