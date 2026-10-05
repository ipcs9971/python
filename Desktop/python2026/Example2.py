# Example 2 — Multiple Objects

# One of the biggest advantages of OOP is that one class can create many objects.

# Problem

# Create an Employee class and create three employees.

class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("----------------")


employee1 = Employee("Rahul", 40000, "IT")

employee2 = Employee("Priya", 50000, "HR")

employee3 = Employee("Amit", 60000, "Finance")


employee1.display()
employee2.display()
employee3.display()


#----------------------------------------------------------------------------------------------------------

# Output
# Name: Rahul
# Salary: 40000
# Department: IT
# ----------------
# Name: Priya
# Salary: 50000
# Department: HR
# ----------------
# Name: Amit
# Salary: 60000
# Department: Finance
# ----------------
# Important idea

# We created only one class:

# class Employee:

# But created three different objects:

# employee1
# employee2
# employee3

# Each object has its own data.

# Employee
#    │
#    ├── employee1
#    │      ├── Rahul
#    │      ├── 40000
#    │      └── IT
#    │
#    ├── employee2
#    │      ├── Priya
#    │      ├── 50000
#    │      └── HR
#    │
#    └── employee3
#           ├── Amit
#           ├── 60000
#           └── Finance

# This is one of the most important reasons we use OOP.