class Employee:
        def __init__(self, name, desig, salary):
            self.name=name
            self.desig=desig
            self.salary=salary
        def displayDetails(self):
            print("Name:", self.name, ",Designation:", self.desig, ",Salary:", self.salary)
e1=Employee("Mohit", "UI/UX", 834567)
e2=Employee("Tom", "AI/ML", 50000)
e3=Employee("Bob", "Technition", 30000)
e4=Employee("Alice", "Director", 25000)
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()
