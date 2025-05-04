student_grades = {"A": 90, "B": 85, "C": 77}
for s in student_grades:
    print(f"Student: {s}")

for s, g in student_grades.items():
    print(f"Name: {s} === Grades: {g}")