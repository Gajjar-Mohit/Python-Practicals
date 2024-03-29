
#Single Inheritance
print("Single Inheritance")
print('------------------------------------------')
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

child = Child("Mohit", 21, 'Sem-4')
print("Name:", child.name)
print("Age:", child.age)
print("Grade:", child.grade)
print('\n')

#Multilevel Inheritance
print("Multilevel Inheritance")
print('------------------------------------------')
class Grandparent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Parent(Grandparent):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

class Child(Parent):
    def __init__(self, name, age, occupation, grade):
        super().__init__(name, age, occupation)
        self.grade = grade

child = Child("Mohit", 21, "Student",'Sem-4')
print("Name:", child.name)
print("Age:", child.age)
print("Occupation:", child.occupation)
print("Grade:", child.grade)
print('\n')

#Multiple Inheritance
print("Multiple Inheritance")
print('------------------------------------------')
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mother:
    def __init__(self, occupation, salary):
        self.occupation = occupation
        self.salary = salary

class Child(Father, Mother):
    def __init__(self, name, age, occupation, salary, grade):
        Father.__init__(self, name, age)
        Mother.__init__(self, occupation, salary)
        self.grade = grade

child = Child("Mohit", 21, "Student",'None','Sem-4')
print("Name:", child.name)
print("Age:", child.age)
print("Occupation:", child.occupation)
print("Salary:", child.salary)
print("Grade:", child.grade)
print('\n')

