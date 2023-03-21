class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def get_grade(self):
        return self.grade

# create two student objects
student1 = Student("Dhruv", 90)
student2 = Student("Rudrax", 80)

# define a function to compare their grades
def compare_grades(student1, student2):
    if student1.get_grade() > student2.get_grade():
        return f"{student1.name} has a higher grade than {student2.name}"
    elif student1.get_grade() < student2.get_grade():
        return f"{student2.name} has a higher grade than {student1.name}"
    else:
        return "Both students have the same grade"

# call the function to compare the grades of the two students
print(compare_grades(student1, student2))