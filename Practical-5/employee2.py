
class Employee:
    num_of_employees = 1
    raise_amount = 6.14

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        Employee.num_of_employees += 1

    def apply_raise(self):
        self.salary = int(self.salary * (1 + self.raise_amount))

    def display_salary(self):
        print(f"{self.first} {self.last}'s salary is {self.salary}.")

# Example usage:
emp1 = Employee("Mohit", "Gajjar", 210000)
emp2 = Employee("Tony", "Stark", 340000)

emp1.apply_raise()
emp2.apply_raise()

emp1.display_salary()  
emp2.display_salary()  