labs_completed = int(input("Enter the number of labs completed: "))
quizzes_completed = int(input("Enter the number of quizzes completed: "))

assignment_grades = []
for i in range(1, 5):
    grade = float(input(f"Enter grade for Assignment {i}: "))
    assignment_grades.append(grade)

midterm_grades = []
for i in range(1, 3):
    grade = float(input(f"Enter grade for Midterm {i}: "))
    midterm_grades.append(grade)

final_exam_grade = float(input("Enter grade for Final Exam: "))
prep_grade = float(input("Enter grade for Midterms and Final Preparation: "))

lab_grade = (labs_completed / 6) * 100
lab_weighted = lab_grade * 0.20

quiz_grade = (quizzes_completed / 6) * 100
quiz_weighted = quiz_grade * 0.15

assignment_average = sum(assignment_grades) / len(assignment_grades)
assignment_weighted = assignment_average * 0.16

midterm_average = sum(midterm_grades) / len(midterm_grades)
midterm_weighted = midterm_average * 0.25

final_weighted = final_exam_grade * 0.18
prep_weighted = prep_grade * 0.06

total_grade = (lab_weighted + quiz_weighted + assignment_weighted + midterm_weighted + final_weighted + prep_weighted)

total_grade = round(total_grade, 2)
print(f"Your grade is: {total_grade}")
