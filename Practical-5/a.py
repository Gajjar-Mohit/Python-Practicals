class Employee:
        def __init__(self, name, desig, salary):
            self.name=name
            self.desig=desig
            self.salary=salary
        def displayDetails(self):
            print("Name:", self.name, ", Designation:", self.desig, ", Salary:", self.salary)
e1=Employee("Dhruv", "ML", 80000)
e2=Employee("Rudrax", "AI", 50000)
e3=Employee("Dhruvil", "BEEE", 30000)
e4=Employee("Royal Care", "Manager", 25000)
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()
