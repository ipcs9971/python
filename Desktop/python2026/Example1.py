# Example 1 — Basic Class and Object
# Problem

# Create a Student class that stores a student's name and age and displays the information.

# Code
class Student:
     def __init__(self, name, age): # constructor method
        self.name = name # instance variable
        self.age = age

    def display(self): # method to display student information
        print("Student Name:", self.name)
        print("Student Age:", self.age)


student1 = Student("Rahul", 21) #   creating an object of the Student class

student1.display()              #    calling the display method on the student1 object


############################EXPlanation##########################

# Step-by-step explanation
# Step 1 — Create a class
# class Student:

# class is used to create a class.

# Student is the class name.

# Think of a class as a blueprint.

# Student class
#      ↓
# Blueprint
# Step 2 — Constructor
# def __init__(self, name, age):

# __init__() is a special method.

# It automatically runs when we create an object.

# For example:

# student1 = Student("Rahul", 21)

# Python automatically calls:

# __init__("Rahul", 21)
# Step 3 — Store the values
# self.name = name
# self.age = age

# Here:

# name → "Rahul"
# age  → 21

# They are stored inside the object.

# Step 4 — What is self?

# self represents the current object.

# For:

# student1 = Student("Rahul", 21)

# Python internally associates:

# self → student1

# So:

# self.name

# means:

# student1.name

# Step 5 — Create a method
# def display(self):

# A function inside a class is called a method.

# Step 6 — Create object
# student1 = Student("Rahul", 21)

# Student = class

# student1 = object

# Class
#   ↓
# Student
#   ↓
# Object
#   ↓
# student1
# Step 7 — Call method
# student1.display()

# This executes:

# display()

# for student1.