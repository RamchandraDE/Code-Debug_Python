""" Ask How many students = 5

Enter a student name = Rama
marks1 = 
marks2 = 
marks3 = 
marks4 = 

Enter name = Anirudh
marks1 = 
marks2 = 
marks3 = 
marks4 = 
"""

dictonary = {}

student_count = int(input("Enter studnets count = "))
for _ in range(student_count):
    marks = []
    name = input("Enter name of student = ")
    sub_count = int(input("Enter sub count = "))
    for i in range(1, sub_count + 1):
        m = int(input(f"Enter marks {i} "))
        marks.append(m)
    dictonary[name] = marks

print(dictonary)
