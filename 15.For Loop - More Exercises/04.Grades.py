import sys
import math
grades_scale = {range(5, sys.maxsize): "top",
                range(4, 5): "above_average",
                range(3, 4): "average",
                range(-sys.maxsize, 3): "fail"
                }
student_level = {"fail": 0,
                 "average": 0,
                 "above_average": 0,
                 "top": 0
                 }

students_count = int(input())
grade_sum = 0
student = ""

for i in range(students_count):
    grade = float(input())
    for key in grades_scale:
        if math.floor(grade) in key:
            student = grades_scale[key]

    if student in student_level:
        student_level[student] += 1

    grade_sum += grade

top_students = (student_level["top"]/students_count) * 100
above_average_students = (student_level["above_average"]/students_count) * 100
average_students = (student_level["average"]/students_count) * 100
failures = (student_level["fail"]/students_count) * 100
average_grade = grade_sum / students_count

print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {above_average_students:.2f}%")
print(f"Between 3.00 and 3.99: {average_students:.2f}%")
print(f"Fail: {failures:.2f}%")
print(f"Average: {average_grade:.2f}")