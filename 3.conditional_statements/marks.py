"""
Ask a single mark from user 
91-100 -> A
81-90 - B
71-80 - C 
1-70 - FAIL
"""

marks = int(input("Enter marks = "))

if marks >= 91 and marks <= 100:
    print("A")
elif marks >= 81 and marks <= 90:
    print("B")
elif marks >= 71 and marks <= 80:
    print("C")
elif marks >= 0 and marks <= 70:
    print("FAIL")

else:
    print("Invalid Marks")
