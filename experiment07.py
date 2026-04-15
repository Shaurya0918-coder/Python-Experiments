class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # Method to display details
    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Marks:", self.marks)

    # Method to calculate grade
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    # Method to check pass/fail
    def is_pass(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"


# Creating objects
s1 = Student("Rahul", 20, 85)
s2 = Student("Anjali", 19, 92)

# Displaying details for Student 1
s1.display()
print("Grade :", s1.grade())
print("Result:", s1.is_pass())

# Displaying details for Student 2
s2.display()
print("Grade :", s2.grade())
print("Result:", s2.is_pass())