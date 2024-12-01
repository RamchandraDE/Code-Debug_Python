"""ask marks from user history
total
percentage

"""

tel = int(input("Telugu marks = "))
hi = int(input("Hindi marks ="))
eng = int(input("English marks ="))
math = int(input("Maths marks ="))
sci = int(input("Science marks ="))

marks = tel + hi + eng + math + sci
percentage = marks / 500 * 100

print(f" Your total marks {marks}")
print(f"Total percentage {percentage :.2f}")
