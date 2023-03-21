class Student:
    def __init__(self, rollNumber, name):
        self.rollNumber = rollNumber
        self.name = name

class Exam(Student):
    def __init__(self, rollNumber, name, subject1, subject2, subject3, subject4, subject5, subject6):
        super().__init__(rollNumber, name)
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.subject4 = subject4
        self.subject5 = subject5
        self.subject6 = subject6
    
class Result(Exam):
    def __init__(self, rollNumber, name, subject1, subject2, subject3, subject4, subject5, subject6):
        super().__init__(rollNumber, name, subject1, subject2, subject3, subject4, subject5, subject6)
        self.totalMarks = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
        
    def displayResult(self):
        print(f"Roll Number: {self.rollNumber}")
        print(f"Name: {self.name}")
        print(f"Subject 1: {self.subject1}")
        print(f"Subject 2: {self.subject2}")
        print(f"Subject 3: {self.subject3}")
        print(f"Subject 4: {self.subject4}")
        print(f"Subject 5: {self.subject5}")
        print(f"Subject 6: {self.subject6}")
        print(f"Total Marks: {self.totalMarks}")
        
# Interactive program
rollNumber = input("Enter Roll Number: ")
name = input("Enter Name: ")
subject1 = int(input("Enter Marks in Subject 1: "))
subject2 = int(input("Enter Marks in Subject 2: "))
subject3 = int(input("Enter Marks in Subject 3: "))
subject4 = int(input("Enter Marks in Subject 4: "))
subject5 = int(input("Enter Marks in Subject 5: "))
subject6 = int(input("Enter Marks in Subject 6: "))

result = Result(rollNumber, name, subject1, subject2, subject3, subject4, subject5, subject6)
result.displayResult()