# 1st que
"""num1: int = int(input("Enter a num1 = "))
num2: int = int(input("Enter a num2 = "))

if num1 % num2 == 0:
    print(f"{num1}is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")"""

# 2nd sol

"""class_attended = int(input("Enter a attended classes = "))
class_held = int(input("Enter a  total class num = "))

percentage = class_attended / class_held * 100

if percentage >= 75:
    print("  You are allowed to sit in the exam hall")
else:
    print("you are not allowed")"""

# 3rd sol

"""num: int = int(input("Enter a num = "))

if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print(f"{num} is div by 2 and 3 but not by 8 ")

else:
    print("not applicable")"""

# 4th sol

"""score: int = int(input("Enter your score = "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")"""

# 5th sol

"""finalAmount = int(input("Final amount = "))

discount = 0
discounted_amount = finalAmount

if finalAmount > 50000:
    discount = 30
elif finalAmount >= 40000 and finalAmount <= 49999:
    discount = 25
elif finalAmount >= 30000 and finalAmount <= 39999:
    discount = 20
elif finalAmount >= 10000 and finalAmount <= 29999:
    discount = 10
else:
    print("No Discount")

if discount > 0:
    discounted_amount = finalAmount - (finalAmount * discount / 100)

print(f"You got {discount}% discount")
print(f"Your final bill is rs {discounted_amount:.2f}")"""

# sol 6
"""num1 = int(input("Enter a num1 = "))
num2 = int(input("Enter a num2 = "))
num3 = int(input("Enter a num3 = "))
num4 = int(input("Enter a num4 = "))

smallest_num = num1

if num2 < smallest_num:
    smallest_num = num2

if num3 < smallest_num:
    smallest_num = num3

if num4 < smallest_num:
    smallest_num = num4

print(f"The smallest number is: {smallest_num}")"""

# sol 7

"""salary = float(input("enter salary = "))

if salary < 10000:
    increment = 5
elif salary >= 10000 and salary <= 20000:
    increment = 10

elif salary >= 20000 and salary <= 50000:
    increment = 15
else:
    increment = 20


increment_salary = (salary * increment) / 100
updated_salary = salary + increment_salary

print(f" the original salary was rs {salary:.2f}")
print(f" your increment percentage {increment}")
print(f" your final salary is {updated_salary:.2f}")"""

# sol 9:


"""year: int = int(input("Enter a year = "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")
"""
