telugu = int(input("Enter telugu marks = "))
hindi = int(input("Enter hindi marks = "))
english = int(input("Enter english marks = "))
math = int(input("Enter math marks = "))
science = int(input("Enter science marks = "))


total = telugu + hindi + english + math + science
print(f"Your total is = {total}")

percentage = total / 500 * 100

print(f"your percentage is = {percentage:.2f}")
