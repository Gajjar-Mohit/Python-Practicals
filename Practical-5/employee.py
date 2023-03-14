# A)
class Employee:
        def __init__(self, name, desig, salary):
            self.name=name
            self.desig=desig
            self.salary=salary
        def displayDetails(self):
            print("Name:", self.name, ", Designation:", self.desig, ", Salary:", self.salary)
e1=Employee("Mohit", "BTECH", 80000)
e2=Employee("Jal", "MSC", 50000)
e3=Employee("Darsh", "SCI", 30000)
e4=Employee("Tony", "Owner", 25000)
print("Details: ")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()
