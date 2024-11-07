"""
ASK a single mark from user
"""

mark = int(input("enter a mark = "))

if mark >= 91 and mark <= 100:
    print(f" Your grade is A")

elif mark >= 81 and mark <= 90:
    print(f"your grade is B")
elif mark >= 71 and mark <= 80:
    print(f"Your grade is C")
elif mark >= 0 and mark <= 70:
    print("FAIL")
else:
    print(f"Invalid marks")
