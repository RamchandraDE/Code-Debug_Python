"""def max_find(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def mini_find(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


num1 = 20
num2 = 25
num3 = 19

max_value = max_find(num1, num2, num3)
mini_value = mini_find(num1, num2, num3)


print(f"The maximum num is {max_value}")
print(f"The minimun num is {mini_value}")"""


def leap_year():
    year = int(input("Enter a year = "))

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


leap_year()


def marks(phy=0, chem=0, eng=0, sci=0, hin=0):
    total = phy + chem + eng + sci + hin
    percentage = (total / 500) * 100
    print(f"your total marks {total}")
    print(f"your percentage {percentage}")


marks(56, 65)
