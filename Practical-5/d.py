class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_grade(self):
        return self.grade

student1 = Student("Mohit", 98)
student2 = Student("Stark", 79)

def compare_grades(student1, student2):
    if student1.get_grade() > student2.get_grade():
        return f"{student1.name} has a higher grade than {student2.name}"
    elif student1.get_grade() < student2.get_grade():
        return f"{student2.name} has a higher grade than {student1.name}"
    else:
        return "Both students have the same grade"

print(compare_grades(student1, student2))