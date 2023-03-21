with open("Practical-9/student.txt", "r") as student_file, open("Practical-9/marks.txt", "r") as marks_file:
    students = []
    for line in student_file:
        students.append(line.strip())
    marks = []
    for line in marks_file:
        marks.append(int(line.strip()))

print("Student\tMarks")
for i in range(len(students)):
    print(students[i] + "\t" + str(marks[i]))
